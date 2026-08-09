#!/usr/bin/env python3
"""Descarga/actualiza mods y resource packs del pack, verificando SHA1. Solo stdlib.

  python3 sync.py            descarga lo que falte o esté corrupto
  python3 sync.py --prune    además borra lo que ya no está en mods.json
  python3 sync.py --verify   solo re-verifica hashes, no descarga nada
  python3 sync.py --deps     valida que cada mod tenga la versión de sus dependencias
  python3 sync.py --install [ruta]   además, copia todo a .minecraft (auto-detecta si falta ruta)
  python3 sync.py --test     autotest de la lógica de rangos de versión

ponytail: 70 líneas en vez de packwiz porque el pack es 100% Modrinth salvo 6 mods.
Si algún día hace falta exportar .mrpack o meter CurseForge de verdad -> usar packwiz.
"""
import hashlib, io, json, os, pathlib, platform, re, shutil, sys, tempfile, tomllib, urllib.request, zipfile

ROOT = pathlib.Path(__file__).parent
DEST = {"mod": "mods", "resourcepack": "resourcepacks", "shaderpack": "shaderpacks"}
UA = {"User-Agent": "terra-incognita-sync/1.0"}


def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def vkey(s):
    """'2.12.36' -> (2,12,36). Las versiones de mods no son semver, así que se
    comparan los números que haya. ponytail: alcanza para rangos de Forge."""
    return tuple(int(n) for n in re.findall(r"\d+", str(s))[:6])


def satisface(ver, rango):
    """¿`ver` cae dentro del rango Maven de Forge? '[1.8.0,)', '[1,2)', '(,3]'."""
    if not rango.strip() or rango.strip() == "*":    # '*' = cualquier versión
        return True
    v = vkey(ver)
    partes = re.findall(r"[\[(][^\[\]()]*[\])]", rango)
    if not partes:
        # sin corchetes es una "versión recomendada" de Maven: vale como mínimo,
        # no como exacta. Forge la trata igual. Ej: amendments pide '1.20-2.16.0'.
        return v >= vkey(rango)
    for parte in partes:
        abre, cierra, cuerpo = parte[0], parte[-1], parte[1:-1]
        lo, _, hi = cuerpo.partition(",")
        if not _:                                    # '[1.2]' = exacto
            if v == vkey(lo):
                return True
            continue
        okl = not lo.strip() or (v >= vkey(lo) if abre == "[" else v > vkey(lo))
        okh = not hi.strip() or (v <= vkey(hi) if cierra == "]" else v < vkey(hi))
        if okl and okh:
            return True
    return False


def leer_mod(datos):
    """[(modId, versión, [(depId, rango, obligatoria)])] de un jar (bytes o ruta).

    Incluye los jars anidados en META-INF/jarjar/: Forge los carga como mods
    propios, así que un `diagonalblocks` embebido cuenta como instalado."""
    salida = []
    with zipfile.ZipFile(datos) as z:
        nombres = z.namelist()
        toml = next((n for n in ("META-INF/mods.toml", "META-INF/neoforge.mods.toml")
                     if n in nombres), None)
        if toml:
            t = tomllib.loads(z.read(toml).decode("utf-8", "replace"))
            for mod in t.get("mods", []):
                ver = str(mod.get("version", "0"))
                if "$" in ver:                       # version="${file.jarVersion}"
                    man = z.read("META-INF/MANIFEST.MF").decode("utf-8", "replace")
                    m = re.search(r"Implementation-Version:\s*(\S+)", man)
                    ver = m.group(1) if m else "0"
                deps = [(d["modId"], d.get("versionRange", ""), d.get("mandatory", True))
                        for d in t.get("dependencies", {}).get(mod["modId"], [])
                        if d["modId"] not in ("forge", "minecraft")]
                salida.append((mod["modId"], ver, deps))
        for n in nombres:
            if n.startswith("META-INF/jarjar/") and n.endswith(".jar"):
                salida += leer_mod(io.BytesIO(z.read(n)))
    return salida


def revisar_deps():
    """Compara lo que cada mod exige contra lo que hay instalado en ./mods."""
    instalado, exige, ilegibles = {}, [], []
    for jar in sorted((ROOT / "mods").glob("*.jar")):
        try:
            mods = leer_mod(jar)
        except Exception as e:
            ilegibles.append(f"{jar.name}: {e}")
            continue
        for mid, ver, deps in mods:
            instalado.setdefault(mid, (ver, jar.name))
            exige += [(mid, jar.name, d, r, o) for d, r, o in deps]

    fallos = []
    for quien, jarname, dep, rango, obligatoria in exige:
        if dep not in instalado:
            if obligatoria:
                fallos.append(f"  FALTA     {dep!r} — lo pide {quien} ({jarname})")
        # el rango vale también para dependencias opcionales YA instaladas
        elif rango and not satisface(instalado[dep][0], rango):
            fallos.append(f"  VERSIÓN   {dep} está en {instalado[dep][0]}, "
                          f"{quien} pide {rango}")
    for l in ilegibles:
        print("  ilegible ", l)
    print("\n".join(fallos) if fallos else "  sin problemas de dependencias")
    print(f"\n{len(instalado)} mods leídos (con los anidados), {len(exige)} dependencias, "
          f"{len(fallos)} problemas")
    return 1 if fallos else 0


def minecraft_dir(sistema=None):
    """Carpeta .minecraft estándar según el SO. CurseForge App/Prism/MultiMC/
    Modrinth App usan carpetas por instancia: para esos, pasar la ruta a mano
    con --install <ruta>."""
    sistema = sistema or platform.system()
    home = pathlib.Path.home()
    if sistema == "Darwin":
        return home / "Library" / "Application Support" / "minecraft"
    if sistema == "Windows":
        return pathlib.Path(os.environ.get("APPDATA", str(home))) / ".minecraft"
    return home / ".minecraft"          # Linux y cualquier otro *nix


def instalar(destino, origen_root=ROOT):
    """Copia mods/resourcepacks/shaderpacks ya sincronizados a una carpeta
    .minecraft real. No borra nada del destino que no sea de este pack: lo que
    el usuario haya agregado a mano en su carpeta real queda intacto. Si un
    archivo pasó a .disabled (o volvió) en el repo, lo renombra del lado del
    destino en vez de duplicarlo."""
    if destino.resolve() == origen_root.resolve():
        print("  el destino es este mismo repo, no tiene sentido")
        return 1
    if not destino.is_dir():
        print(f"  no existe {destino} -- pasá la ruta correcta con --install <ruta> "
              f"(CurseForge App/Prism/MultiMC/Modrinth App usan carpetas por instancia)")
        return 1
    copiados = renombrados = al_dia = 0
    for carpeta in DEST.values():
        origen = origen_root / carpeta
        if not origen.is_dir():
            continue
        objetivo = destino / carpeta
        objetivo.mkdir(exist_ok=True)
        for src in sorted(origen.iterdir()):
            if not src.is_file() or src.name == ".DS_Store":
                continue
            base = src.name.removesuffix(".disabled")
            apagado = src.name != base
            dst = objetivo / src.name
            opuesto = objetivo / (base if apagado else base + ".disabled")
            if opuesto.exists() and not dst.exists():
                print(f"  renombrando (.disabled)  {opuesto.name} -> {dst.name}")
                opuesto.rename(dst)
                renombrados += 1
            if dst.exists() and sha1(dst) == sha1(src):
                al_dia += 1
                continue
            print(f"  copiando  {carpeta}/{src.name}")
            shutil.copy2(src, dst)
            copiados += 1
    print(f"\n{copiados} copiados / {renombrados} renombrados (.disabled) / "
          f"{al_dia} ya al día -> {destino}")
    return 0


def autotest():
    """Los rangos de versión son la única lógica no obvia acá. Que falle fuerte."""
    casos = [("2.11.33", "[2.12.36,)", False), ("2.12.36", "[2.12.36,)", True),
             ("15.10.0.30", "[15.20.0.106,)", False), ("15.48.0.180", "[15.20.0.106,)", True),
             ("8.1.4", "*", True), ("1.0", "", True), ("1.5", "[1.0,2.0)", True),
             ("2.0", "[1.0,2.0)", False), ("2.0", "[1.0,2.0]", True),
             ("1.0", "(1.0,2.0]", False), ("47.4.20", "[47,)", True),
             # sin corchetes = mínimo, no exacto (Maven "recommended version")
             ("1.20-2.16.34", "1.20-2.16.0", True), ("1.20-2.15.0", "1.20-2.16.0", False),
             ("2.16.0", "2.16.0", True)]
    for ver, rango, esperado in casos:
        assert satisface(ver, rango) is esperado, f"satisface({ver!r}, {rango!r})"
    print(f"  {len(casos)} casos OK")

    home = pathlib.Path.home()
    assert minecraft_dir("Darwin") == home / "Library" / "Application Support" / "minecraft"
    assert minecraft_dir("Linux") == home / ".minecraft"
    assert minecraft_dir("Windows").name == ".minecraft"
    print("  minecraft_dir(): 3 casos OK")

    with tempfile.TemporaryDirectory() as t:
        t = pathlib.Path(t)
        origen, destino = t / "repo", t / "minecraft"
        (origen / "mods").mkdir(parents=True)
        destino.mkdir()
        jar = origen / "mods" / "Foo.jar"
        jar.write_bytes(b"contenido")

        assert instalar(t / "no-existe", origen_root=origen) == 1
        assert instalar(destino, origen_root=origen) == 0
        assert (destino / "mods" / "Foo.jar").read_bytes() == b"contenido"

        jar.rename(origen / "mods" / "Foo.jar.disabled")
        instalar(destino, origen_root=origen)
        assert (destino / "mods" / "Foo.jar.disabled").exists()
        assert not (destino / "mods" / "Foo.jar").exists()

        (origen / "mods" / "Foo.jar.disabled").rename(origen / "mods" / "Foo.jar")
        instalar(destino, origen_root=origen)
        assert (destino / "mods" / "Foo.jar").exists()
        assert not (destino / "mods" / "Foo.jar.disabled").exists()
    print("  instalar(): copiar + toggle .disabled sin duplicar OK")
    return 0


def main(argv):
    if "--test" in argv:
        return autotest()
    if "--deps" in argv:
        return revisar_deps()
    prune, verify = "--prune" in argv, "--verify" in argv
    rows = json.loads((ROOT / "mods.json").read_text(encoding="utf-8"))
    wanted = {r["filename"]: r for r in rows if r.get("url")}
    manual = [r for r in rows if not r.get("url")]
    for d in DEST.values():
        (ROOT / d).mkdir(exist_ok=True)

    ok = bad = new = off = 0
    for name, r in sorted(wanted.items()):
        dest = ROOT / DEST[r.get("type", "mod")] / name
        # Forge ignora los .jar.disabled: es la forma nativa de apagar un mod
        # sin sacarlo del pack. Si está así, no lo bajamos de nuevo.
        if dest.with_name(name + ".disabled").exists():
            off += 1
            continue
        if dest.exists() and sha1(dest) == r["sha1_remote"]:
            ok += 1
            continue
        if verify:
            print(f"  FALTA/CORRUPTO  {name}")
            bad += 1
            continue
        print(f"  bajando  {name}")
        req = urllib.request.Request(r["url"], headers=UA)
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
        got = hashlib.sha1(data).hexdigest()
        if got != r["sha1_remote"]:
            print(f"  !! hash no coincide en {name} ({got}) - no se guarda")
            bad += 1
            continue
        dest.write_bytes(data)
        new += 1

    strays = [p for d in DEST.values() for p in (ROOT / d).iterdir()
              if p.is_file() and p.name != ".DS_Store"
              and p.name not in wanted
              and p.name.removesuffix(".disabled") not in wanted]
    for p in strays:
        if prune:
            print(f"  borrando sobrante  {p.name}")
            p.unlink()
        else:
            print(f"  sobrante (usa --prune para borrar)  {p.name}")

    print(f"\n{ok} ya estaban / {new} descargados / {bad} con problemas / "
          f"{len(strays)} sobrantes" + (f" / {off} apagados (.disabled)" if off else ""))
    if manual:
        print(f"\nDescargar a mano en ./mods (solo están en CurseForge):")
        for r in manual:
            print(f"  - {r['title']}")

    codigo = 1 if bad else 0
    if "--install" in argv:
        i = argv.index("--install")
        ruta = argv[i + 1] if i + 1 < len(argv) and not argv[i + 1].startswith("--") else None
        destino = pathlib.Path(ruta).expanduser() if ruta else minecraft_dir()
        print()
        codigo = instalar(destino) or codigo
    return codigo


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
