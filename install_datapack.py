#!/usr/bin/env python3
"""Instala los datapacks de ./datapacks en el mundo de un save real.

  python3 install_datapack.py "Nombre del mundo"
  python3 install_datapack.py "Nombre del mundo" --dest /ruta/a/tu/instancia

ponytail: aparte de sync.py porque los datapacks son por-mundo, no globales a toda
la instalación de Minecraft como mods/resourcepacks/shaderpacks.
"""
import pathlib, shutil, sys
import sync

ROOT = pathlib.Path(__file__).parent


def main(argv):
    if not argv or argv[0].startswith("--"):
        print(__doc__)
        return 1
    mundo = argv[0]
    ruta = argv[argv.index("--dest") + 1] if "--dest" in argv else None
    base = pathlib.Path(ruta).expanduser() if ruta else sync.minecraft_dir()

    if not base.is_dir():
        print(f"  no existe {base} -- pasá --dest <ruta> si usás "
              f"CurseForge App/Prism/MultiMC/Modrinth App")
        return 1

    saves = base / "saves"
    if not (saves / mundo).is_dir():
        print(f"  no encontré el mundo {mundo!r} en {saves}")
        if saves.is_dir():
            disponibles = sorted(p.name for p in saves.iterdir() if p.is_dir())
            if disponibles:
                print("  mundos disponibles:")
                for d in disponibles:
                    print(f"    - {d}")
        return 1

    destino = saves / mundo / "datapacks"
    destino.mkdir(exist_ok=True)
    instalados = []
    for dp in sorted(p for p in (ROOT / "datapacks").iterdir() if p.is_dir()):
        shutil.copytree(dp, destino / dp.name, dirs_exist_ok=True)
        instalados.append(dp.name)

    print(f"\n{len(instalados)} datapack(s) instalado(s) en {destino}:")
    for n in instalados:
        print(f"  - {n}")
    print("\nSolo afecta a los chunks que se generen de ahora en más: los que ya "
          "existen no cambian. Si el mundo ya está abierto, corré /reload; si no, "
          "basta con volver a entrar.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
