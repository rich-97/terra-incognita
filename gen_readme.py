#!/usr/bin/env python3
"""Genera el README.md del modpack desde mods.json + descripciones en español."""
import json, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).parent
rows = json.loads((ROOT / "mods.json").read_text())

# grupo, descripción en español. Clave = nombre del .jar original.
D = {
 # --- Mundo, biomas y estructuras ---
 "terralith": ("world", "Casi 100 biomas nuevos generados solo con bloques vanilla: montañas, cuevas y paisajes muy superiores a los de base."),
 "incendium": ("world", "Rehace el Nether entero: biomas nuevos, estructuras difíciles y armas exclusivas."),
 "bygone-nether": ("world", "Estructuras propias para cada bioma del Nether, con mobs que las habitan."),
 "the-bumblezone": ("world", "Dimensión nueva llena de abejas. Si les robás la miel se enojan de verdad."),
 "towns-and-towers": ("world", "Aldeas rediseñadas por bioma, puestos de saqueadores nuevos y barcos navegables."),
 "when-dungeons-arise": ("world", "Mazmorras y estructuras roguelike enormes repartidas por el mundo. De los mods de estructuras más grandes que hay."),
 "when-dungeons-arise-seven-seas": ("world", "Expansión de Dungeons Arise: barcos y estructuras perdidas en el mar."),
 "the-graveyard-forge": ("world", "Cementerios, criptas y catacumbas con mobs y jefes de temática necro."),
 "SkyVillages-1.0.4-1.19.2-1.20.1-forge-release.jar": ("world", "Aldeas flotantes en el cielo, con su propio loot y peligro de caída."),
 "deeperdarker": ("world", "Expande el Deep Dark con una dimensión nueva (Otherside), bloques, armaduras y un jefe."),
 "nullscape": ("world", "Rehace el End entero: islas alienígenas y terreno vertical que no parece Minecraft. Cierra el trío con Terralith e Incendium."),
 "structory": ("world", "Estructuras atmosféricas con lore ligero, repartidas por bioma. Hechas por los mismos autores de Terralith."),
 "structory-towers": ("world", "Torres temáticas por bioma. Complemento opcional de Structory."),
 "yungs-extras": ("world", "Estructuras y detalles vanilla+ sueltos que YUNG no metió en sus otros mods."),
 "alexs-caves": ("world", "Seis biomas de cueva raros bajo la superficie, cada uno con su ecosistema y sus peligros. El jar más pesado del pack (75 MB)."),
 "mystical-oak-tree": ("world", "Un roble parlante tipo NPC con 300+ líneas de lore y consejos."),
 "large-ore-deposits": ("world", "Depósitos de mineral gigantes y rarísimos: minar vuelve a valer la pena."),
 "yungs-better-dungeons": ("world", "Rediseño completo de las mazmorras vanilla (las salas de spawner)."),
 "yungs-better-mineshafts": ("world", "Minas abandonadas rediseñadas: más grandes, variadas y con loot decente."),
 "yungs-better-strongholds": ("world", "Fortalezas del End rediseñadas, con bibliotecas y salas temáticas."),
 "yungs-better-desert-temples": ("world", "Templos del desierto rediseñados, con un jefe propio."),
 "yungs-better-jungle-temples": ("world", "Templos de la jungla rediseñados, con puzzles y trampas nuevas."),
 "yungs-better-ocean-monuments": ("world", "Monumentos oceánicos rediseñados y mucho más grandes."),
 "yungs-better-witch-huts": ("world", "Chozas de bruja rediseñadas en los pantanos."),
 "yungs-better-nether-fortresses": ("world", "Fortalezas del Nether rediseñadas, mucho más laberínticas."),
 "yungs-better-end-island": ("world", "Rehace la isla principal del End y la pelea contra el dragón."),
 "yungs-bridges": ("world", "Puentes naturales generados sobre ríos y barrancos."),

 # --- Mobs, jefes y combate ---
 "alexs-mobs": ("combat", "85+ mobs nuevos con el mismo nivel de detalle que Ice and Fire — es del mismo autor y comparte Citadel."),
 "ribbits": ("combat", "Aldeas de ranas músicas en los pantanos, con sus propios trades."),
 "ice-and-fire-dragons": ("combat", "Dragones (fuego, hielo, rayo), hipogrifos, cíclopes, sirenas y demás criaturas míticas. El mod más pesado del pack."),
 "bosses-of-mass-destruction-forge": ("combat", "Cuatro jefes opcionales con peleas de mecánicas propias, no solo bolsas de vida."),
 "gateways-to-eternity": ("combat", "Portales invocables que lanzan oleadas de mobs a cambio de recompensas."),
 "creeper-overhaul": ("combat", "Un creeper distinto por bioma, cada uno con comportamiento y drop propio."),
 "friends-and-foes-forge": ("combat", "Los mobs que perdieron las mob votes: Copper Golem, Moobloom, Iceologer, Rascal, etc."),
 "illager-invasion": ("combat", "Variantes nuevas de illagers con habilidades propias y un jefe."),
 "it-takes-a-pillage": ("combat", "Los pillagers se organizan: fortalezas, unidades nuevas y raids más serias."),
 "villagersplus": ("combat", "Tipos de aldeano nuevos, con trades y estaciones de trabajo propias."),
 "goblintraders-forge-1.20.1-1.9.3.jar": ("combat", "Goblins comerciantes que aparecen en cuevas y en el Nether con trades raros."),
 "tiny-skeletons": ("combat", "Esqueletos bebé, rápidos y molestos."),
 "from-the-fog": ("combat", "Herobrine acechándote de a poco: sonidos, apariciones y bloques movidos. Mod de terror."),
 "enhanced-boss-bars-mod": ("combat", "Barras de jefe rediseñadas y más informativas. Solo cliente."),
 "spartan-weaponry": ("combat", "Arsenal enorme: lanzas, dagas, mazas, ballestas, boomerangs y más."),
 "more-bows-restrung": ("combat", "Arcos nuevos con estadísticas y efectos distintos."),
 "weaponmaster": ("combat", "Muestra las armas de tu hotbar colgadas del personaje, cada tipo en su sitio."),
 "apothic-attributes": ("combat", "Atributos nuevos (crítico, robo de vida, armadura penetrante) más una GUI para verlos."),
 "Gobber2-Forge-1.20.1-2.8.9.jar": ("combat", "Mineral endgame 'gobber' con herramientas, armaduras y utilidades muy potentes."),
 "Craftable_Elytra[REMASTERED][2.2]1.20.1.jar": ("combat", "Permite craftear la elytra en vez de tener que ir al End a buscarla."),

 # --- Almacenamiento e inventario ---
 "sophisticated-backpacks": ("storage", "Mochilas mejorables con filtros, autorecogida, crafteo interno y colores. El mod de mochilas de referencia."),
 "sophisticated-core": ("storage", "Librería base de los mods Sophisticated."),
 "storagedrawers": ("storage", "Cajones que guardan enormes cantidades de un solo ítem, con acceso rápido."),
 "ender-storage": ("storage", "Cofres y tanques enlazados por código de color, accesibles desde cualquier dimensión."),
 "bag-of-holding": ("storage", "Una bolsa que guarda de todo, alternativa simple a las mochilas."),
 "echo-chest": ("storage", "Cofre que absorbe automáticamente los ítems que caen cerca."),
 "nether-chested": ("storage", "Cofre del Nether que apila 8 veces más de lo normal."),
 "easy-shulker-boxes": ("storage", "Meter y sacar cosas de las shulker box directo desde el inventario, sin colocarlas."),
 "carry-on": ("storage", "Levantar y cargar cofres llenos, hornos y mobs con las manos."),
 "corpse": ("storage", "Al morir dejás un cadáver con todo tu inventario en vez de ítems tirados que despawnean."),
 "xp-tome": ("storage", "Un libro para guardar y retirar experiencia."),

 # --- Calidad de vida e interfaz ---
 "travelers-titles": ("qol", "Títulos tipo RPG al entrar a un bioma o dimensión. Es lo que le faltaba al resource pack Visual Titles."),
 "inventory-essentials": ("qol", "Ordena el inventario y cualquier cofre con una tecla. También mover y tirar stacks completos de un golpe."),
 "distanthorizons": ("gameplay", "Render distance enorme: genera y dibuja terreno simplificado (LOD) mucho más allá de tu distancia normal. **Opcional** — mirá la nota abajo."),
 "amendments": ("gameplay", "Faroles de pared, velas de calavera, macetas y estandartes de techo. Salieron de Supplementaries en su 2.8.0 y viven acá."),
 "supplementaries": ("gameplay", "Vanilla+ enorme: jarros, carteles indicadores, veletas, faroles de cuerda, pizarras y decenas de bloques más."),
 "balm": ("lib", "Librería de abstracción entre loaders. La necesita Inventory Essentials."),
 "jei": ("qol", "Buscador de ítems y recetas. Imprescindible en cualquier pack con 100 mods."),
 "just-enough-effect-descriptions-jeed": ("qol", "Plugin de JEI que explica qué hace cada efecto de poción y de dónde sale."),
 "appleskin": ("qol", "Muestra saturación y cuánta hambre te da cada comida antes de comerla."),
 "xaeros-minimap": ("qol", "Minimapa en la esquina con waypoints, mobs y jugadores."),
 "xaeros-world-map": ("qol", "Mapa a pantalla completa de todo lo explorado. Se integra con el minimapa."),
 "legendary-tooltips": ("qol", "Tooltips con marco decorado según la rareza del ítem, y más opciones de formato."),
 "held-item-tooltips": ("qol", "Muestra encantamientos y contenido del ítem que tenés en la mano, sobre la hotbar."),
 "effect-insights": ("qol", "Describe los efectos de pociones y comidas directamente en el tooltip."),
 "pick-up-notifier": ("qol", "Aviso en pantalla de todo lo que vas recogiendo."),
 "easy-anvils": ("qol", "Yunques sin el castigo de reparación acumulativo y con costes justos."),
 "easy-magic": ("qol", "La mesa de encantar conserva los ítems al cerrarla y permite re-tirar encantamientos."),
 "enchanting-infuser": ("qol", "Mesa de encantar alternativa: elegís el encantamiento que querés, sin azar."),
 "trading-post": ("qol", "Bloque para comerciar con todos los aldeanos cercanos a la vez."),
 "visual-workbench": ("qol", "La mesa de crafteo guarda los ítems dentro y los muestra encima."),
 "horse-expert": ("qol", "Ver las estadísticas reales de velocidad, salto y salud de un caballo."),
 "armor-statues": ("qol", "Menú completo para posar armor stands. Funciona hasta en servers vanilla."),
 "straw-statues": ("qol", "Estatuas con la skin de cualquier jugador para decorar builds."),
 "better-third-person": ("qol", "Cámara en tercera persona que rota independiente del cuerpo. Solo cliente."),
 "tl_skin_cape_forge_1.20_1.20.1-1.32.jar": ("qol", "Skins y capas de TLauncher en cuentas no premium. Solo cliente, específico de TLauncher."),

 # --- Mecánicas, movilidad y ambiente ---
 "comforts": ("gameplay", "Sacos de dormir (dormís sin cambiar el punto de respawn) y hamacas."),
 "exposure": ("gameplay", "Cámara de fotos con revelado real: sacás fotos y las colgás como cuadros."),
 "hang-glider": ("gameplay", "Ala delta para planear antes de conseguir la elytra."),
 "do-a-barrel-roll": ("gameplay", "Control de vuelo con elytra tipo simulador: alabeo, giros y acrobacias."),
 "easy-emerald": ("gameplay", "Forma sencilla de craftear esmeraldas, más bloques y herramientas de esmeralda."),
 "diagonal-fences": ("gameplay", "Las cercas conectan en diagonal. Suena tonto hasta que construís algo."),
 "fallingleavesforge": ("gameplay", "Partículas de hojas cayendo de los árboles. Solo cliente."),
 "ambientsounds": ("gameplay", "Sonido ambiente dinámico según bioma, clima y hora. Solo cliente, y es el jar más pesado (85 MB)."),
 "just-zoom": ("qol", "Zoom con una tecla, con el factor ajustable desde la rueda del mouse. Solo cliente."),

 # --- Librerías (no aportan contenido) ---
 "geckolib": ("lib", "Motor de animaciones 3D. Lo usan casi todos los mods de mobs."),
 "citadel": ("lib", "Librería de Ice and Fire y otros mods de Alex."),
 "placebo": ("lib", "Librería de los mods de Shadows (Gateways, Apothic)."),
 "puzzles-lib": ("lib", "Librería de todos los mods de Fuzs (los 'Easy*', tooltips, etc)."),
 "yungs-api": ("lib", "Librería de todos los mods de YUNG."),
 "moonlight": ("lib", "Librería de registro dinámico y datapacks en runtime."),
 "creativecore": ("lib", "Librería de AmbientSounds y otros mods de CreativeMD."),
 "cloth-config": ("lib", "Librería de pantallas de configuración."),
 "codechicken-lib": ("lib", "Librería de render, matemática 3D y networking. La usa Ender Storage."),
 "iceberg": ("lib", "Librería de eventos y utilidades de render (Legendary Tooltips)."),
 "prism-lib": ("lib", "Librería de manejo de color. Depende de Iceberg."),
 "cerbons-api": ("lib", "Librería de los mods de CERBON (Enhanced Boss Bars)."),
 "cristel-lib": ("lib", "Librería para configurar estructuras y datapacks en runtime."),
 "forgeendertech": ("lib", "Librería base de los mods de Endertech (Large Ore Deposits)."),
 "resourceful-config": ("lib", "Librería de configuración multiplataforma."),
 "framework-forge-1.20.1-0.7.6.jar": ("lib", "Librería de MrCrayfish (Goblin Traders y otros)."),
 "entity-model-features": ("lib", "Permite modelos de entidad personalizados (CEM) sin OptiFine. Lo necesitan Fresh Animations y Better Dogs."),
 "entitytexturefeatures": ("lib", "Permite texturas de entidad variables y emisivas (CET) sin OptiFine. Va de la mano con EMF."),
 "embeddium": ("qol", "Port de Sodium para Forge: reescribe el renderizado y sube bastante los FPS. Sirve aunque nunca uses shaders."),
 "konkrete": ("lib", "Librería de utilidades de interfaz. La necesita Just Zoom."),
 "oculus": ("qol", "Port de Iris para Forge: es lo que hace que la carpeta `shaderpacks/` exista. Necesita Embeddium."),
}

# Resource packs: descripción en español. Clave = nombre del archivo original.
RP = {
 "faithful-32x": "Las texturas vanilla al doble de resolución, respetando el estilo original. La base sobre la que van los demás.",
 "ModernArch": None,
 "xalis-bushy-leaves": "Hojas más frondosas y con volumen: los árboles dejan de verse planos.",
 "ore-variants": "Cada mineral se ve distinto según la piedra en la que está (piedra, deepslate, nether).",
 "rays-3d-rails": "Rieles con modelo 3D en vez de calcomanías planas en el suelo.",
 "fresh-animations": "Animaciones nuevas para todos los mobs vanilla: giran la cabeza, parpadean, reaccionan. Cambia muchísimo cómo se siente el mundo.",
 "better-dogs": "Razas de perro reales para los lobos domesticados, cada una con su textura.",
 "enhanced-boss-bars": "Texturas para el mod Enhanced Boss Bars: una barra distinta por jefe.",
 "eclectic-trove-legendary-tooltips": "Marcos de tooltip para Legendary Tooltips, uno por nivel de rareza.",
 "fire-rekindled": "Fuego, antorchas y lava reanimados, con más cuadros y mejor color. Cubre también los bloques de Supplementaries.",
 "visual-travelers-titles": "Los títulos de Traveler's Titles con tipografía y animación propias, en vez del texto plano de vanilla.",
 "icon-xaeros": "Iconos propios para las entidades y waypoints del minimapa de Xaero's.",
}
RP = {k: v for k, v in RP.items() if v}

GRUPOS = [
    ("world",    "🗺️ Mundo, biomas y estructuras", "Generación de terreno y todo lo que hay para explorar."),
    ("combat",   "⚔️ Mobs, jefes y combate", "Enemigos nuevos, peleas y armas."),
    ("storage",  "🎒 Almacenamiento e inventario", "Dónde meter todo lo que juntás."),
    ("qol",      "🧭 Calidad de vida e interfaz", "Información en pantalla y menos fricción."),
    ("gameplay", "🪂 Mecánicas, movilidad y ambiente", "Cosas nuevas para hacer y ver."),
    ("lib",      "📚 Librerías y dependencias", "No aportan contenido: otros mods los necesitan para funcionar."),
]

mods = [r for r in rows if r.get("type", "mod") == "mod"]
packs = [r for r in rows if r.get("type") == "resourcepack"]
shaders = [r for r in rows if r.get("type") == "shaderpack"]
by_file = {(r.get("slug") or r["file"]): r for r in mods}
for etiqueta, claves, desc in [("mods", set(by_file), D), ("resource packs", {(r.get("slug") or r["file"]) for r in packs}, RP)]:
    assert not claves - set(desc), f"{etiqueta} sin descripción: {sorted(claves - set(desc))}"
    assert not set(desc) - claves, f"descripción sobrante en {etiqueta}: {sorted(set(desc) - claves)}"


def link(r):
    t = r.get("title") or r["file"]
    if r.get("slug"):
        return f'[{t}](https://modrinth.com/mod/{r["slug"]})'
    url = "https://www.curseforge.com/minecraft/search?search=" + urllib.parse.quote(t.split(" (")[0])
    return f"[{t}]({url})"


def tabla(files):
    out = ["| Mod | Qué hace | Fuente |", "|---|---|---|"]
    for f in sorted(files, key=lambda f: (by_file[f].get("title") or f).lower()):
        r = by_file[f]
        src = "Modrinth" if r.get("slug") else "CurseForge"
        if r.get("server_side") == "unsupported":
            src += " · cliente"
        if r.get("opcional"):
            src += " · **opcional**"
        out.append(f'| {link(r)} | {D[f][1]} | {src} |')
    return "\n".join(out)


auto = [r for r in rows if r.get("url")]
manual = [r for r in rows if not r.get("url")]
peso = round(sum(r["size"] for r in rows) / 1e6)

secciones = []
for key, titulo, sub in GRUPOS:
    files = [f for f in by_file if D[f][0] == key]
    secciones.append(f"### {titulo}\n\n*{sub}* — **{len(files)} mods**\n\n{tabla(files)}")

tabla_rp = "\n".join(["| Resource pack | Qué hace |", "|---|---|"] + [
    f'| [{r["title"]}](https://modrinth.com/resourcepack/{r["slug"]}) | {RP[r.get("slug") or r["file"]]} |'
    for r in sorted(packs, key=lambda r: r["title"].lower())])

SH = {"bsl-shaders": "El mejor equilibrio entre cómo se ve y cuánto cuesta, con un menú de "
                     "configuración enorme para bajarle cosas si te pesa.",
      "bliss-shader": "Edit de Chocapic13. Más bonito y más caro que BSL: mejor agua, "
                      "volumétricos y cielo."}
tabla_sh = "\n".join(["| Shader | Dónde corre | Qué es |", "|---|---|---|"] + [
    f'| [{r["title"]} v{r["version_number"]}](https://modrinth.com/shader/{r["slug"]}) '
    f'| **{r["plataforma"]}** | {SH[r["slug"]]} |'
    for r in sorted(shaders, key=lambda r: r["title"].lower())])

README = f"""# Terra Incognita

> *«…y de aquí en adelante, tierra desconocida.»*

Modpack de exploración para **Minecraft 1.20.1** con **Forge**: {len(mods)} mods que rehacen
el mundo vanilla entero — cada estructura, las tres dimensiones y buena parte de los mobs.
Sin tech ni automatización. Solo salir a ver qué hay, y sobrevivirlo.

Este repo **no contiene los archivos** — guarda la lista con versión, URL y hash de cada uno
([`mods.json`](mods.json)) y un script que los descarga. Así el repo pesa kilobytes en vez de
{peso} MB, los diffs muestran exactamente qué cambió, y nadie redistribuye mods ajenos.

| | |
|---|---|
| **Minecraft** | 1.20.1 |
| **Mod loader** | Forge 47.x (última recomendada) |
| **Mods** | {len(mods)} ({len(auto)} automáticos + {len(manual)} manuales) |
| **Resource packs** | {len(packs)} |
| **Shaders** | {len(shaders)} (opcional, uno por sistema) |
| **RAM recomendada** | 6 GB mínimo, 8 GB cómodo |
| **Peso en disco** | ~{peso} MB |

---

## Instalación

### 1. Descargar todo

```bash
git clone <URL-DE-ESTE-REPO>
cd terra-incognita
python3 sync.py
```

Descarga todo en `./mods`, `./resourcepacks` y `./shaderpacks`, verificando el SHA1 de
cada archivo. Si ya los tenías, solo baja lo que cambió.

### 2. Los {len(manual)} mods que faltan

No están en Modrinth, hay que bajarlos a mano de CurseForge y ponerlos en `./mods`:

{chr(10).join(f"- **{r['title']}**" for r in manual)}

### 3. Según tu launcher

**TLauncher**
1. Instalá **Forge 1.20.1** desde el propio launcher.
2. Copiá `mods/`, `resourcepacks/` y `shaderpacks/` a
   `~/Library/Application Support/minecraft/` (Windows: `%APPDATA%\\.minecraft\\`).
3. Asignale 6–8 GB de RAM en Configuración → Java.

**CurseForge App / Prism / MultiMC / Modrinth App**
1. Creá una instancia de Minecraft 1.20.1 con Forge.
2. Abrí la carpeta de la instancia y copiá las tres carpetas adentro.
3. Subí la RAM a 6–8 GB en las opciones de la instancia.

### 4. Activar los resource packs

Los resource packs se descargan pero **no se activan solos**. Dentro del juego:
Opciones → Resource Packs → moverlos a la derecha. El orden importa: **Faithful abajo**
(es la base) y los específicos arriba.

---

## Mods

{chr(10).join(chr(10) + s for s in secciones)}

---

## Resource packs

Los {len(packs)} son compatibles con 1.20.1 y con los mods de este pack. Todos opcionales.

{tabla_rp}

> **Fresh Animations y Better Dogs necesitan EMF + ETF**, que ya están incluidos en los mods.
> Son el reemplazo de OptiFine en Forge — sin ellos los packs se instalan pero no hacen nada.

---

## Apagar un mod sin sacarlo del pack

Agregale `.disabled` al final del nombre del archivo:

```bash
mv mods/DistantHorizons-2.4.5-b-1.20.1-fabric-forge.jar{{,.disabled}}
```

Forge ignora nativamente cualquier `.jar.disabled`, y `sync.py` lo respeta: no te lo
vuelve a bajar ni lo borra con `--prune`. Te lo reporta como *apagado*. Para prenderlo
de vuelta, sacale el sufijo.

**Distant Horizons** es el candidato obvio: genera terreno lejano usando el generador de
chunks del juego, y con Terralith + Incendium + los mods de estructuras eso es caro. Las
primeras horas de un mundo nuevo va a estar trabajando fuerte. Si te molesta, se apaga.

Dos formas de bajarle el volumen sin llegar a eso:

- **Desde el juego**: Opciones → Distant Horizons → *Enable Rendering*. Se apaga el
  dibujado sin tocar archivos.
- **Ajustando**: en un M-series con 16 GB, empezá con render distance de Minecraft en
  8–12 chunks y el LOD distance de DH en 64–96 (no 512), y limitale los threads de
  generación a 3–4 en vez de dejarlo tomar todos los núcleos.

---

## Shaders

Van los dos, elegís según en qué máquina estés jugando:

{tabla_sh}

Funcionan gracias a **Oculus** (el port de Iris para Forge) + **Embeddium** (el port de Sodium),
que ya están en la lista de mods. Embeddium por sí solo sube los FPS aunque nunca actives un shader.

Se activan en Opciones → Video Settings → Shader Packs.

> ### ⚠️ Por qué hay uno para cada sistema
>
> Los shaders modernos usan **compute shaders**, que necesitan **OpenGL 4.3**. macOS tope en
> **4.1** y Apple ya no lo actualiza, así que en Mac no arrancan — no importa qué GPU tengas.
>
> - **Bliss v2.1.2** usa 8 → Windows y Linux, donde se ve mejor.
> - **BSL v8.2.09** usa 0 → anda en todos lados, incluido macOS. Está **fijada a propósito**:
>   la v10.x agregó compute shaders, así que actualizarla la rompería en Mac.
>
> Por lo mismo quedaron afuera **Aurora's Shaders** y **Bloop**.
>
> Si dejás de jugar en Mac, subí BSL a la última cambiándole `version_number`, `url`,
> `sha1_remote` y `filename` en `mods.json`.

---

## Actualizar

```bash
git pull
python3 sync.py --prune
python3 sync.py --deps     # antes de abrir el juego
```

`--prune` borra de `mods/` los jars que ya no están en la lista.
Para verificar que no se corrompió nada sin descargar: `python3 sync.py --verify`.

Para actualizar un mod, editá su entrada en `mods.json` (`version_number`, `url`,
`sha1_remote`, `filename`) y commiteá. El diff de git muestra exactamente qué cambió.
Después corré `gen_readme.py` para que la lista de acá arriba siga al día.

> ### Corré `--deps` después de tocar cualquier versión
>
> Subir un mod sin subir sus dependencias es la forma más fácil de romper el pack: el
> juego crashea en el arranque con "requires X 2.12.36 or above". `--deps` lee el
> `mods.toml` de cada jar (incluidos los anidados en `META-INF/jarjar/`) y compara lo
> que cada mod exige contra lo que hay instalado, antes de que lo descubra Minecraft.

---

## Notas

- Todo el pack es **Forge 1.20.1**. Antes de agregar un mod, confirmá que su página
  liste `Forge` y `1.20.1` — si no, no carga.
- En los resource packs mirá el `pack_format`: **15** es 1.20–1.20.1. Uno más nuevo o
  más viejo suele cargar igual, pero Minecraft te avisa y puede faltar alguna textura.
- Los mods marcados **· cliente** no hacen falta en el servidor.
- Las librerías no aportan contenido: si sacás el mod que las usa, se pueden sacar también.
- Ice and Fire, AmbientSounds y The Bumblezone son los tres jars más pesados del pack.

## Licencia

Cada mod pertenece a su autor y conserva su propia licencia. Este repo solo contiene
la lista y los scripts.
"""

(ROOT / "README.md").write_text(README)
print(f"README.md escrito: {len(mods)} mods + {len(packs)} resource packs + {len(shaders)} shader, {peso} MB")
for key, titulo, _ in GRUPOS:
    print(f"  {titulo}: {sum(1 for f in by_file if D[f][0] == key)}")
