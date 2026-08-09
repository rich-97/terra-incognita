#!/usr/bin/env python3
"""Descarga/actualiza mods y resource packs del pack, verificando SHA1. Solo stdlib.

  python3 sync.py            descarga lo que falte o esté corrupto
  python3 sync.py --prune    además borra lo que ya no está en mods.json
  python3 sync.py --verify   solo re-verifica hashes, no descarga nada

ponytail: 70 líneas en vez de packwiz porque el pack es 100% Modrinth salvo 6 mods.
Si algún día hace falta exportar .mrpack o meter CurseForge de verdad -> usar packwiz.
"""
import hashlib, json, pathlib, sys, urllib.request

ROOT = pathlib.Path(__file__).parent
DEST = {"mod": "mods", "resourcepack": "resourcepacks", "shaderpack": "shaderpacks"}
UA = {"User-Agent": "terra-incognita-sync/1.0"}


def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv):
    prune, verify = "--prune" in argv, "--verify" in argv
    rows = json.loads((ROOT / "mods.json").read_text())
    wanted = {r["filename"]: r for r in rows if r.get("url")}
    manual = [r for r in rows if not r.get("url")]
    for d in DEST.values():
        (ROOT / d).mkdir(exist_ok=True)

    ok = bad = new = 0
    for name, r in sorted(wanted.items()):
        dest = ROOT / DEST[r.get("type", "mod")] / name
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
              if p.is_file() and p.name not in wanted and p.name != ".DS_Store"]
    for p in strays:
        if prune:
            print(f"  borrando sobrante  {p.name}")
            p.unlink()
        else:
            print(f"  sobrante (usa --prune para borrar)  {p.name}")

    print(f"\n{ok} ya estaban / {new} descargados / {bad} con problemas / "
          f"{len(strays)} sobrantes")
    if manual:
        print(f"\nDescargar a mano en ./mods (solo están en CurseForge):")
        for r in manual:
            print(f"  - {r['title']}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
