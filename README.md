# Modpack de Minecraft 1.20.1 (Forge)

Modpack personal de **94 mods** para Minecraft **1.20.1** con **Forge**.
Enfoque: exploración, estructuras, mobs y calidad de vida. Sin tech/automatización.

Este repo **no contiene los `.jar`** — guarda la lista con versión, URL y hash de cada mod
([`mods.json`](mods.json)) y un script que los descarga. Así el repo pesa kilobytes en vez de
271 MB, los diffs muestran exactamente qué mod cambió, y nadie redistribuye mods ajenos.

| | |
|---|---|
| **Minecraft** | 1.20.1 |
| **Mod loader** | Forge 47.x (última recomendada) |
| **Mods** | 94 (88 automáticos + 6 manuales) |
| **RAM recomendada** | 6 GB mínimo, 8 GB cómodo |
| **Peso en disco** | ~271 MB solo en mods |

---

## Instalación

### 1. Descargar los mods

```bash
git clone <URL-DE-ESTE-REPO>
cd minecraft-modpack
python3 sync.py
```

Descarga los 88 mods de Modrinth en `./mods`, verificando el SHA1 de cada uno.
Si ya los tenías, solo baja lo que cambió.

### 2. Los 6 mods que faltan

No están en Modrinth, hay que bajarlos a mano de CurseForge y ponerlos en `./mods`:

- **Craftable Elytra [REMASTERED]**
- **Framework (MrCrayfish)**
- **Gobber 2**
- **Goblin Traders**
- **Sky Villages**
- **TLSkinCape (TLauncher)**

### 3. Según tu launcher

**TLauncher**
1. Instalá **Forge 1.20.1** desde el propio launcher.
2. Copiá el contenido de `mods/` a `~/Library/Application Support/minecraft/mods`
   (Windows: `%APPDATA%\.minecraft\mods`).
3. Asignale 6–8 GB de RAM en Configuración → Java.

**CurseForge App / Prism / MultiMC / Modrinth App**
1. Creá una instancia de Minecraft 1.20.1 con Forge.
2. Abrí la carpeta de la instancia y copiá `mods/` adentro.
3. Subí la RAM a 6–8 GB en las opciones de la instancia.

---

## Mods


### 🗺️ Mundo, biomas y estructuras

*Generación de terreno y todo lo que hay para explorar.* — **22 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [Bygone Nether](https://modrinth.com/mod/bygone-nether) | Estructuras propias para cada bioma del Nether, con mobs que las habitan. | Modrinth |
| [Deeper and Darker](https://modrinth.com/mod/deeperdarker) | Expande el Deep Dark con una dimensión nueva (Otherside), bloques, armaduras y un jefe. | Modrinth |
| [Incendium Legacy](https://modrinth.com/mod/incendium) | Rehace el Nether entero: biomas nuevos, estructuras difíciles y armas exclusivas. | Modrinth |
| [Large Ore Deposits](https://modrinth.com/mod/large-ore-deposits) | Depósitos de mineral gigantes y rarísimos: minar vuelve a valer la pena. | Modrinth |
| [Mystical Oak Tree](https://modrinth.com/mod/mystical-oak-tree) | Un roble parlante tipo NPC con 300+ líneas de lore y consejos. | Modrinth |
| [Sky Villages](https://www.curseforge.com/minecraft/search?search=Sky%20Villages) | Aldeas flotantes en el cielo, con su propio loot y peligro de caída. | CurseForge |
| [Terralith](https://modrinth.com/mod/terralith) | Casi 100 biomas nuevos generados solo con bloques vanilla: montañas, cuevas y paisajes muy superiores a los de base. | Modrinth |
| [The Bumblezone - NeoForge/Forge](https://modrinth.com/mod/the-bumblezone) | Dimensión nueva llena de abejas. Si les robás la miel se enojan de verdad. | Modrinth |
| [The Graveyard (FORGE/NEOFORGE)](https://modrinth.com/mod/the-graveyard-forge) | Cementerios, criptas y catacumbas con mobs y jefes de temática necro. | Modrinth |
| [Towns and Towers](https://modrinth.com/mod/towns-and-towers) | Aldeas rediseñadas por bioma, puestos de saqueadores nuevos y barcos navegables. | Modrinth |
| [When Dungeons Arise](https://modrinth.com/mod/when-dungeons-arise) | Mazmorras y estructuras roguelike enormes repartidas por el mundo. De los mods de estructuras más grandes que hay. | Modrinth |
| [When Dungeons Arise: Seven Seas](https://modrinth.com/mod/when-dungeons-arise-seven-seas) | Expansión de Dungeons Arise: barcos y estructuras perdidas en el mar. | Modrinth |
| [YUNG's Better Desert Temples](https://modrinth.com/mod/yungs-better-desert-temples) | Templos del desierto rediseñados, con un jefe propio. | Modrinth |
| [YUNG's Better Dungeons](https://modrinth.com/mod/yungs-better-dungeons) | Rediseño completo de las mazmorras vanilla (las salas de spawner). | Modrinth |
| [YUNG's Better End Island](https://modrinth.com/mod/yungs-better-end-island) | Rehace la isla principal del End y la pelea contra el dragón. | Modrinth |
| [YUNG's Better Jungle Temples](https://modrinth.com/mod/yungs-better-jungle-temples) | Templos de la jungla rediseñados, con puzzles y trampas nuevas. | Modrinth |
| [YUNG's Better Mineshafts](https://modrinth.com/mod/yungs-better-mineshafts) | Minas abandonadas rediseñadas: más grandes, variadas y con loot decente. | Modrinth |
| [YUNG's Better Nether Fortresses](https://modrinth.com/mod/yungs-better-nether-fortresses) | Fortalezas del Nether rediseñadas, mucho más laberínticas. | Modrinth |
| [YUNG's Better Ocean Monuments](https://modrinth.com/mod/yungs-better-ocean-monuments) | Monumentos oceánicos rediseñados y mucho más grandes. | Modrinth |
| [YUNG's Better Strongholds](https://modrinth.com/mod/yungs-better-strongholds) | Fortalezas del End rediseñadas, con bibliotecas y salas temáticas. | Modrinth |
| [YUNG's Better Witch Huts](https://modrinth.com/mod/yungs-better-witch-huts) | Chozas de bruja rediseñadas en los pantanos. | Modrinth |
| [YUNG's Bridges](https://modrinth.com/mod/yungs-bridges) | Puentes naturales generados sobre ríos y barrancos. | Modrinth |

### ⚔️ Mobs, jefes y combate

*Enemigos nuevos, peleas y armas.* — **18 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [Apothic Attributes](https://modrinth.com/mod/apothic-attributes) | Atributos nuevos (crítico, robo de vida, armadura penetrante) más una GUI para verlos. | Modrinth |
| [Bosses of Mass Destruction Forge](https://modrinth.com/mod/bosses-of-mass-destruction-forge) | Cuatro jefes opcionales con peleas de mecánicas propias, no solo bolsas de vida. | Modrinth |
| [Craftable Elytra [REMASTERED]](https://www.curseforge.com/minecraft/search?search=Craftable%20Elytra%20%5BREMASTERED%5D) | Permite craftear la elytra en vez de tener que ir al End a buscarla. | CurseForge |
| [Creeper Overhaul](https://modrinth.com/mod/creeper-overhaul) | Un creeper distinto por bioma, cada uno con comportamiento y drop propio. | Modrinth |
| [Enhanced Boss Bars](https://modrinth.com/mod/enhanced-boss-bars-mod) | Barras de jefe rediseñadas y más informativas. Solo cliente. | Modrinth · cliente |
| [Friends&Foes (Forge/NeoForge)](https://modrinth.com/mod/friends-and-foes-forge) | Los mobs que perdieron las mob votes: Copper Golem, Moobloom, Iceologer, Rascal, etc. | Modrinth |
| [From The Fog](https://modrinth.com/mod/from-the-fog) | Herobrine acechándote de a poco: sonidos, apariciones y bloques movidos. Mod de terror. | Modrinth |
| [Gateways to Eternity](https://modrinth.com/mod/gateways-to-eternity) | Portales invocables que lanzan oleadas de mobs a cambio de recompensas. | Modrinth |
| [Gobber 2](https://www.curseforge.com/minecraft/search?search=Gobber%202) | Mineral endgame 'gobber' con herramientas, armaduras y utilidades muy potentes. | CurseForge |
| [Goblin Traders](https://www.curseforge.com/minecraft/search?search=Goblin%20Traders) | Goblins comerciantes que aparecen en cuevas y en el Nether con trades raros. | CurseForge |
| [Ice and Fire](https://modrinth.com/mod/ice-and-fire-dragons) | Dragones (fuego, hielo, rayo), hipogrifos, cíclopes, sirenas y demás criaturas míticas. El mod más pesado del pack. | Modrinth |
| [Illager Invasion](https://modrinth.com/mod/illager-invasion) | Variantes nuevas de illagers con habilidades propias y un jefe. | Modrinth |
| [It Takes a Pillage](https://modrinth.com/mod/it-takes-a-pillage) | Los pillagers se organizan: fortalezas, unidades nuevas y raids más serias. | Modrinth |
| [More Bows: Restrung!](https://modrinth.com/mod/more-bows-restrung) | Arcos nuevos con estadísticas y efectos distintos. | Modrinth |
| [Spartan Weaponry](https://modrinth.com/mod/spartan-weaponry) | Arsenal enorme: lanzas, dagas, mazas, ballestas, boomerangs y más. | Modrinth |
| [Tiny Skeletons](https://modrinth.com/mod/tiny-skeletons) | Esqueletos bebé, rápidos y molestos. | Modrinth |
| [VillagersPlus](https://modrinth.com/mod/villagersplus) | Tipos de aldeano nuevos, con trades y estaciones de trabajo propias. | Modrinth |
| [YDM's Weapon Master](https://modrinth.com/mod/weaponmaster) | Muestra las armas de tu hotbar colgadas del personaje, cada tipo en su sitio. | Modrinth |

### 🎒 Almacenamiento e inventario

*Dónde meter todo lo que juntás.* — **11 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [Bag Of Holding](https://modrinth.com/mod/bag-of-holding) | Una bolsa que guarda de todo, alternativa simple a las mochilas. | Modrinth |
| [Carry On](https://modrinth.com/mod/carry-on) | Levantar y cargar cofres llenos, hornos y mobs con las manos. | Modrinth |
| [Corpse](https://modrinth.com/mod/corpse) | Al morir dejás un cadáver con todo tu inventario en vez de ítems tirados que despawnean. | Modrinth |
| [Easy Shulker Boxes](https://modrinth.com/mod/easy-shulker-boxes) | Meter y sacar cosas de las shulker box directo desde el inventario, sin colocarlas. | Modrinth |
| [Echo Chest](https://modrinth.com/mod/echo-chest) | Cofre que absorbe automáticamente los ítems que caen cerca. | Modrinth |
| [Ender Storage](https://modrinth.com/mod/ender-storage) | Cofres y tanques enlazados por código de color, accesibles desde cualquier dimensión. | Modrinth |
| [Nether Chested](https://modrinth.com/mod/nether-chested) | Cofre del Nether que apila 8 veces más de lo normal. | Modrinth |
| [Sophisticated Backpacks](https://modrinth.com/mod/sophisticated-backpacks) | Mochilas mejorables con filtros, autorecogida, crafteo interno y colores. El mod de mochilas de referencia. | Modrinth |
| [Sophisticated Core](https://modrinth.com/mod/sophisticated-core) | Librería base de los mods Sophisticated. | Modrinth |
| [Storage Drawers](https://modrinth.com/mod/storagedrawers) | Cajones que guardan enormes cantidades de un solo ítem, con acceso rápido. | Modrinth |
| [XP Tome](https://modrinth.com/mod/xp-tome) | Un libro para guardar y retirar experiencia. | Modrinth |

### 🧭 Calidad de vida e interfaz

*Información en pantalla y menos fricción.* — **19 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [AppleSkin](https://modrinth.com/mod/appleskin) | Muestra saturación y cuánta hambre te da cada comida antes de comerla. | Modrinth |
| [Armor Statues](https://modrinth.com/mod/armor-statues) | Menú completo para posar armor stands. Funciona hasta en servers vanilla. | Modrinth |
| [Better Third Person](https://modrinth.com/mod/better-third-person) | Cámara en tercera persona que rota independiente del cuerpo. Solo cliente. | Modrinth · cliente |
| [Easy Anvils](https://modrinth.com/mod/easy-anvils) | Yunques sin el castigo de reparación acumulativo y con costes justos. | Modrinth |
| [Easy Magic](https://modrinth.com/mod/easy-magic) | La mesa de encantar conserva los ítems al cerrarla y permite re-tirar encantamientos. | Modrinth |
| [Effect Insights](https://modrinth.com/mod/effect-insights) | Describe los efectos de pociones y comidas directamente en el tooltip. | Modrinth · cliente |
| [Enchanting Infuser](https://modrinth.com/mod/enchanting-infuser) | Mesa de encantar alternativa: elegís el encantamiento que querés, sin azar. | Modrinth |
| [Held Item Tooltips](https://modrinth.com/mod/held-item-tooltips) | Muestra encantamientos y contenido del ítem que tenés en la mano, sobre la hotbar. | Modrinth · cliente |
| [Horse Expert](https://modrinth.com/mod/horse-expert) | Ver las estadísticas reales de velocidad, salto y salud de un caballo. | Modrinth |
| [Just Enough Effect Descriptions (JEED)](https://modrinth.com/mod/just-enough-effect-descriptions-jeed) | Plugin de JEI que explica qué hace cada efecto de poción y de dónde sale. | Modrinth · cliente |
| [Just Enough Items (JEI)](https://modrinth.com/mod/jei) | Buscador de ítems y recetas. Imprescindible en cualquier pack con 100 mods. | Modrinth |
| [Legendary Tooltips](https://modrinth.com/mod/legendary-tooltips) | Tooltips con marco decorado según la rareza del ítem, y más opciones de formato. | Modrinth · cliente |
| [Pick Up Notifier](https://modrinth.com/mod/pick-up-notifier) | Aviso en pantalla de todo lo que vas recogiendo. | Modrinth |
| [Straw Statues](https://modrinth.com/mod/straw-statues) | Estatuas con la skin de cualquier jugador para decorar builds. | Modrinth |
| [TLSkinCape (TLauncher)](https://www.curseforge.com/minecraft/search?search=TLSkinCape) | Skins y capas de TLauncher en cuentas no premium. Solo cliente, específico de TLauncher. | CurseForge |
| [Trading Post](https://modrinth.com/mod/trading-post) | Bloque para comerciar con todos los aldeanos cercanos a la vez. | Modrinth |
| [Visual Workbench](https://modrinth.com/mod/visual-workbench) | La mesa de crafteo guarda los ítems dentro y los muestra encima. | Modrinth |
| [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap) | Minimapa en la esquina con waypoints, mobs y jugadores. | Modrinth |
| [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) | Mapa a pantalla completa de todo lo explorado. Se integra con el minimapa. | Modrinth |

### 🪂 Mecánicas, movilidad y ambiente

*Cosas nuevas para hacer y ver.* — **8 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [AmbientSounds](https://modrinth.com/mod/ambientsounds) | Sonido ambiente dinámico según bioma, clima y hora. Solo cliente, y es el jar más pesado (85 MB). | Modrinth · cliente |
| [Comforts](https://modrinth.com/mod/comforts) | Sacos de dormir (dormís sin cambiar el punto de respawn) y hamacas. | Modrinth |
| [Diagonal Fences](https://modrinth.com/mod/diagonal-fences) | Las cercas conectan en diagonal. Suena tonto hasta que construís algo. | Modrinth |
| [Do a Barrel Roll](https://modrinth.com/mod/do-a-barrel-roll) | Control de vuelo con elytra tipo simulador: alabeo, giros y acrobacias. | Modrinth |
| [Easy Emerald](https://modrinth.com/mod/easy-emerald) | Forma sencilla de craftear esmeraldas, más bloques y herramientas de esmeralda. | Modrinth |
| [Exposure](https://modrinth.com/mod/exposure) | Cámara de fotos con revelado real: sacás fotos y las colgás como cuadros. | Modrinth |
| [Falling Leaves (NeoForge/Forge)](https://modrinth.com/mod/fallingleavesforge) | Partículas de hojas cayendo de los árboles. Solo cliente. | Modrinth · cliente |
| [Hang Glider](https://modrinth.com/mod/hang-glider) | Ala delta para planear antes de conseguir la elytra. | Modrinth |

### 📚 Librerías y dependencias

*No aportan contenido: otros mods los necesitan para funcionar.* — **16 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [CERBON's API](https://modrinth.com/mod/cerbons-api) | Librería de los mods de CERBON (Enhanced Boss Bars). | Modrinth |
| [Citadel](https://modrinth.com/mod/citadel) | Librería de Ice and Fire y otros mods de Alex. | Modrinth |
| [Cloth Config API](https://modrinth.com/mod/cloth-config) | Librería de pantallas de configuración. | Modrinth |
| [CodeChicken Lib](https://modrinth.com/mod/codechicken-lib) | Librería de render, matemática 3D y networking. La usa Ender Storage. | Modrinth |
| [CreativeCore](https://modrinth.com/mod/creativecore) | Librería de AmbientSounds y otros mods de CreativeMD. | Modrinth |
| [Cristel Lib](https://modrinth.com/mod/cristel-lib) | Librería para configurar estructuras y datapacks en runtime. | Modrinth |
| [ForgeEndertech](https://modrinth.com/mod/forgeendertech) | Librería base de los mods de Endertech (Large Ore Deposits). | Modrinth |
| [Framework (MrCrayfish)](https://www.curseforge.com/minecraft/search?search=Framework) | Librería de MrCrayfish (Goblin Traders y otros). | CurseForge |
| [Geckolib](https://modrinth.com/mod/geckolib) | Motor de animaciones 3D. Lo usan casi todos los mods de mobs. | Modrinth |
| [Iceberg](https://modrinth.com/mod/iceberg) | Librería de eventos y utilidades de render (Legendary Tooltips). | Modrinth |
| [Moonlight Lib](https://modrinth.com/mod/moonlight) | Librería de registro dinámico y datapacks en runtime. | Modrinth |
| [Placebo](https://modrinth.com/mod/placebo) | Librería de los mods de Shadows (Gateways, Apothic). | Modrinth |
| [Prism](https://modrinth.com/mod/prism-lib) | Librería de manejo de color. Depende de Iceberg. | Modrinth · cliente |
| [Puzzles Lib](https://modrinth.com/mod/puzzles-lib) | Librería de todos los mods de Fuzs (los 'Easy*', tooltips, etc). | Modrinth |
| [Resourceful Config](https://modrinth.com/mod/resourceful-config) | Librería de configuración multiplataforma. | Modrinth |
| [YUNG's API](https://modrinth.com/mod/yungs-api) | Librería de todos los mods de YUNG. | Modrinth |

---

## Descartados

Estos jars estaban en la carpeta original pero **no deben ir al pack**:

| Archivo | Problema |
|---|---|
| `PuzzlesLib-v8.0.24-1.20.1-Forge.jar` | Versión vieja **duplicada** de Puzzles Lib. Dejá solo la v8.1.21. |
| `Scout-2.0.4+1.20.1.jar` | Slots extra de inventario vía bolsas — build de **Fabric**, no carga en Forge. |
| `Zoomify-2.14.0+1.20.1.jar` | Zoom configurable — mod **solo Fabric**, no existe versión Forge. |
| `adventurez-1.4.20.jar` | Jefe final y criaturas nuevas — pero este jar es la build de **Fabric**, no carga en Forge. |
| `llibrary-1.7.20-1.12.2.jar` | Librería vieja compilada para **Minecraft 1.12.2**. Puede romper el arranque. |
| `torchesntrinkets-0.2-1.20.1-4.jar` | Antorchas y faroles colgados del cinturón — build de **Fabric**, no carga en Forge. |

---

## Actualizar

```bash
git pull
python3 sync.py --prune
```

`--prune` borra de `mods/` los jars que ya no están en la lista.
Para verificar que no se corrompió nada sin descargar: `python3 sync.py --verify`.

Para actualizar un mod, editá su entrada en `mods.json` (`version_number`, `url`,
`sha1_remote`, `filename`) y commiteá. El diff de git muestra exactamente qué cambió.

---

## Notas

- **Forge y Fabric no se mezclan.** Este pack es Forge; un jar de Fabric simplemente no carga.
- Los mods marcados **· cliente** no hacen falta en el servidor.
- Las librerías no aportan contenido: si sacás el mod que las usa, se pueden sacar también.
- Ice and Fire, AmbientSounds y The Bumblezone son los tres jars más pesados del pack.

## Licencia

Cada mod pertenece a su autor y conserva su propia licencia. Este repo solo contiene
la lista y los scripts.
