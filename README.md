# Terra Incognita

> *«…y de aquí en adelante, tierra desconocida.»*

Modpack de exploración para **Minecraft 1.20.1** con **Forge**: 112 mods que rehacen
el mundo vanilla entero — cada estructura, las tres dimensiones y buena parte de los mobs.
Sin tech ni automatización. Solo salir a ver qué hay, y sobrevivirlo.

Este repo **no contiene los archivos** — guarda la lista con versión, URL y hash de cada uno
([`mods.json`](mods.json)) y un script que los descarga. Así el repo pesa kilobytes en vez de
373 MB, los diffs muestran exactamente qué cambió, y nadie redistribuye mods ajenos.

| | |
|---|---|
| **Minecraft** | 1.20.1 |
| **Mod loader** | Forge 47.x (última recomendada) |
| **Mods** | 112 (118 automáticos + 6 manuales) |
| **Resource packs** | 11 |
| **Shaders** | 1 (opcional) |
| **RAM recomendada** | 6 GB mínimo, 8 GB cómodo |
| **Peso en disco** | ~373 MB |

---

## Instalación

### 1. Descargar todo

```bash
git clone <URL-DE-ESTE-REPO>
cd terra-incognita
python3 sync.py          # en Windows: py sync.py
```

Necesita **Python 3.11 o superior** (usa `tomllib`, que entró en la 3.11). No instala
dependencias: es todo librería estándar. Funciona igual en macOS, Linux y Windows.

Descarga todo en `./mods`, `./resourcepacks` y `./shaderpacks`, verificando el SHA1 de
cada archivo. Si ya los tenías, solo baja lo que cambió.

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
2. Copiá `mods/`, `resourcepacks/` y `shaderpacks/` a
   `~/Library/Application Support/minecraft/` (Windows: `%APPDATA%\.minecraft\`).
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


### 🗺️ Mundo, biomas y estructuras

*Generación de terreno y todo lo que hay para explorar.* — **26 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [Bygone Nether](https://modrinth.com/mod/bygone-nether) | Estructuras propias para cada bioma del Nether, con mobs que las habitan. | Modrinth |
| [Deeper and Darker](https://modrinth.com/mod/deeperdarker) | Expande el Deep Dark con una dimensión nueva (Otherside), bloques, armaduras y un jefe. | Modrinth |
| [Incendium Legacy](https://modrinth.com/mod/incendium) | Rehace el Nether entero: biomas nuevos, estructuras difíciles y armas exclusivas. | Modrinth |
| [Large Ore Deposits](https://modrinth.com/mod/large-ore-deposits) | Depósitos de mineral gigantes y rarísimos: minar vuelve a valer la pena. | Modrinth |
| [Mystical Oak Tree](https://modrinth.com/mod/mystical-oak-tree) | Un roble parlante tipo NPC con 300+ líneas de lore y consejos. | Modrinth |
| [Nullscape](https://modrinth.com/mod/nullscape) | Rehace el End entero: islas alienígenas y terreno vertical que no parece Minecraft. Cierra el trío con Terralith e Incendium. | Modrinth |
| [Sky Villages](https://www.curseforge.com/minecraft/search?search=Sky%20Villages) | Aldeas flotantes en el cielo, con su propio loot y peligro de caída. | CurseForge |
| [Structory](https://modrinth.com/mod/structory) | Estructuras atmosféricas con lore ligero, repartidas por bioma. Hechas por los mismos autores de Terralith. | Modrinth |
| [Structory: Towers](https://modrinth.com/mod/structory-towers) | Torres temáticas por bioma. Complemento opcional de Structory. | Modrinth |
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
| [YUNG's Extras](https://modrinth.com/mod/yungs-extras) | Estructuras y detalles vanilla+ sueltos que YUNG no metió en sus otros mods. | Modrinth |

### ⚔️ Mobs, jefes y combate

*Enemigos nuevos, peleas y armas.* — **20 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [Alex's Mobs](https://modrinth.com/mod/alexs-mobs) | 85+ mobs nuevos con el mismo nivel de detalle que Ice and Fire — es del mismo autor y comparte Citadel. | Modrinth |
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
| [Ribbits](https://modrinth.com/mod/ribbits) | Aldeas de ranas músicas en los pantanos, con sus propios trades. | Modrinth |
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

*Información en pantalla y menos fricción.* — **24 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [AppleSkin](https://modrinth.com/mod/appleskin) | Muestra saturación y cuánta hambre te da cada comida antes de comerla. | Modrinth |
| [Armor Statues](https://modrinth.com/mod/armor-statues) | Menú completo para posar armor stands. Funciona hasta en servers vanilla. | Modrinth |
| [Better Third Person](https://modrinth.com/mod/better-third-person) | Cámara en tercera persona que rota independiente del cuerpo. Solo cliente. | Modrinth · cliente |
| [Easy Anvils](https://modrinth.com/mod/easy-anvils) | Yunques sin el castigo de reparación acumulativo y con costes justos. | Modrinth |
| [Easy Magic](https://modrinth.com/mod/easy-magic) | La mesa de encantar conserva los ítems al cerrarla y permite re-tirar encantamientos. | Modrinth |
| [Effect Insights](https://modrinth.com/mod/effect-insights) | Describe los efectos de pociones y comidas directamente en el tooltip. | Modrinth · cliente |
| [Embeddium](https://modrinth.com/mod/embeddium) | Port de Sodium para Forge: reescribe el renderizado y sube bastante los FPS. Sirve aunque nunca uses shaders. | Modrinth · cliente |
| [Enchanting Infuser](https://modrinth.com/mod/enchanting-infuser) | Mesa de encantar alternativa: elegís el encantamiento que querés, sin azar. | Modrinth |
| [Held Item Tooltips](https://modrinth.com/mod/held-item-tooltips) | Muestra encantamientos y contenido del ítem que tenés en la mano, sobre la hotbar. | Modrinth · cliente |
| [Horse Expert](https://modrinth.com/mod/horse-expert) | Ver las estadísticas reales de velocidad, salto y salud de un caballo. | Modrinth |
| [Inventory Essentials](https://modrinth.com/mod/inventory-essentials) | Ordena el inventario y cualquier cofre con una tecla. También mover y tirar stacks completos de un golpe. | Modrinth |
| [Just Enough Effect Descriptions (JEED)](https://modrinth.com/mod/just-enough-effect-descriptions-jeed) | Plugin de JEI que explica qué hace cada efecto de poción y de dónde sale. | Modrinth · cliente |
| [Just Enough Items (JEI)](https://modrinth.com/mod/jei) | Buscador de ítems y recetas. Imprescindible en cualquier pack con 100 mods. | Modrinth |
| [Just Zoom](https://modrinth.com/mod/just-zoom) | Zoom con una tecla, con el factor ajustable desde la rueda del mouse. Solo cliente. | Modrinth · cliente |
| [Legendary Tooltips](https://modrinth.com/mod/legendary-tooltips) | Tooltips con marco decorado según la rareza del ítem, y más opciones de formato. | Modrinth · cliente |
| [Oculus](https://modrinth.com/mod/oculus) | Port de Iris para Forge: es lo que hace que la carpeta `shaderpacks/` exista. Necesita Embeddium. | Modrinth · cliente |
| [Pick Up Notifier](https://modrinth.com/mod/pick-up-notifier) | Aviso en pantalla de todo lo que vas recogiendo. | Modrinth |
| [Straw Statues](https://modrinth.com/mod/straw-statues) | Estatuas con la skin de cualquier jugador para decorar builds. | Modrinth |
| [TLSkinCape (TLauncher)](https://www.curseforge.com/minecraft/search?search=TLSkinCape) | Skins y capas de TLauncher en cuentas no premium. Solo cliente, específico de TLauncher. | CurseForge |
| [Trading Post](https://modrinth.com/mod/trading-post) | Bloque para comerciar con todos los aldeanos cercanos a la vez. | Modrinth |
| [Traveler's Titles](https://modrinth.com/mod/travelers-titles) | Títulos tipo RPG al entrar a un bioma o dimensión. Es lo que le faltaba al resource pack Visual Titles. | Modrinth · cliente |
| [Visual Workbench](https://modrinth.com/mod/visual-workbench) | La mesa de crafteo guarda los ítems dentro y los muestra encima. | Modrinth |
| [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap) | Minimapa en la esquina con waypoints, mobs y jugadores. | Modrinth |
| [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) | Mapa a pantalla completa de todo lo explorado. Se integra con el minimapa. | Modrinth |

### 🪂 Mecánicas, movilidad y ambiente

*Cosas nuevas para hacer y ver.* — **11 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [AmbientSounds](https://modrinth.com/mod/ambientsounds) | Sonido ambiente dinámico según bioma, clima y hora. Solo cliente, y es el jar más pesado (85 MB). | Modrinth · cliente |
| [Amendments](https://modrinth.com/mod/amendments) | Faroles de pared, velas de calavera, macetas y estandartes de techo. Salieron de Supplementaries en su 2.8.0 y viven acá. | Modrinth |
| [Comforts](https://modrinth.com/mod/comforts) | Sacos de dormir (dormís sin cambiar el punto de respawn) y hamacas. | Modrinth |
| [Diagonal Fences](https://modrinth.com/mod/diagonal-fences) | Las cercas conectan en diagonal. Suena tonto hasta que construís algo. | Modrinth |
| [Distant Horizons](https://modrinth.com/mod/distanthorizons) | Render distance enorme: genera y dibuja terreno simplificado (LOD) mucho más allá de tu distancia normal. **Opcional** — mirá la nota abajo. | Modrinth · **opcional** |
| [Do a Barrel Roll](https://modrinth.com/mod/do-a-barrel-roll) | Control de vuelo con elytra tipo simulador: alabeo, giros y acrobacias. | Modrinth |
| [Easy Emerald](https://modrinth.com/mod/easy-emerald) | Forma sencilla de craftear esmeraldas, más bloques y herramientas de esmeralda. | Modrinth |
| [Exposure](https://modrinth.com/mod/exposure) | Cámara de fotos con revelado real: sacás fotos y las colgás como cuadros. | Modrinth |
| [Falling Leaves (NeoForge/Forge)](https://modrinth.com/mod/fallingleavesforge) | Partículas de hojas cayendo de los árboles. Solo cliente. | Modrinth · cliente |
| [Hang Glider](https://modrinth.com/mod/hang-glider) | Ala delta para planear antes de conseguir la elytra. | Modrinth |
| [Supplementaries](https://modrinth.com/mod/supplementaries) | Vanilla+ enorme: jarros, carteles indicadores, veletas, faroles de cuerda, pizarras y decenas de bloques más. | Modrinth |

### 📚 Librerías y dependencias

*No aportan contenido: otros mods los necesitan para funcionar.* — **20 mods**

| Mod | Qué hace | Fuente |
|---|---|---|
| [[EMF] Entity Model Features](https://modrinth.com/mod/entity-model-features) | Permite modelos de entidad personalizados (CEM) sin OptiFine. Lo necesitan Fresh Animations y Better Dogs. | Modrinth · cliente |
| [[ETF] Entity Texture Features](https://modrinth.com/mod/entitytexturefeatures) | Permite texturas de entidad variables y emisivas (CET) sin OptiFine. Va de la mano con EMF. | Modrinth · cliente |
| [Balm](https://modrinth.com/mod/balm) | Librería de abstracción entre loaders. La necesita Inventory Essentials. | Modrinth |
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
| [Konkrete](https://modrinth.com/mod/konkrete) | Librería de utilidades de interfaz. La necesita Just Zoom. | Modrinth |
| [Moonlight Lib](https://modrinth.com/mod/moonlight) | Librería de registro dinámico y datapacks en runtime. | Modrinth |
| [Placebo](https://modrinth.com/mod/placebo) | Librería de los mods de Shadows (Gateways, Apothic). | Modrinth |
| [Prism](https://modrinth.com/mod/prism-lib) | Librería de manejo de color. Depende de Iceberg. | Modrinth · cliente |
| [Puzzles Lib](https://modrinth.com/mod/puzzles-lib) | Librería de todos los mods de Fuzs (los 'Easy*', tooltips, etc). | Modrinth |
| [Resourceful Config](https://modrinth.com/mod/resourceful-config) | Librería de configuración multiplataforma. | Modrinth |
| [YUNG's API](https://modrinth.com/mod/yungs-api) | Librería de todos los mods de YUNG. | Modrinth |

---

## Resource packs

Los 11 son compatibles con 1.20.1 y con los mods de este pack. Todos opcionales.

| Resource pack | Qué hace |
|---|---|
| [Better Dogs](https://modrinth.com/resourcepack/better-dogs) | Razas de perro reales para los lobos domesticados, cada una con su textura. |
| [Eclectic Trove (Legendary Tooltips)](https://modrinth.com/resourcepack/eclectic-trove-legendary-tooltips) | Marcos de tooltip para Legendary Tooltips, uno por nivel de rareza. |
| [Enhanced Boss Bars](https://modrinth.com/resourcepack/enhanced-boss-bars) | Texturas para el mod Enhanced Boss Bars: una barra distinta por jefe. |
| [Faithful 32x](https://modrinth.com/resourcepack/faithful-32x) | Las texturas vanilla al doble de resolución, respetando el estilo original. La base sobre la que van los demás. |
| [Fire Rekindled](https://modrinth.com/resourcepack/fire-rekindled) | Fuego, antorchas y lava reanimados, con más cuadros y mejor color. Cubre también los bloques de Supplementaries. |
| [Fresh Animations](https://modrinth.com/resourcepack/fresh-animations) | Animaciones nuevas para todos los mobs vanilla: giran la cabeza, parpadean, reaccionan. Cambia muchísimo cómo se siente el mundo. |
| [Icon Xaero's](https://modrinth.com/resourcepack/icon-xaeros) | Iconos propios para las entidades y waypoints del minimapa de Xaero's. |
| [Ore Variants](https://modrinth.com/resourcepack/ore-variants) | Cada mineral se ve distinto según la piedra en la que está (piedra, deepslate, nether). |
| [RAY's 3D Rails](https://modrinth.com/resourcepack/rays-3d-rails) | Rieles con modelo 3D en vez de calcomanías planas en el suelo. |
| [Visual Traveler's Titles](https://modrinth.com/resourcepack/visual-travelers-titles) | Los títulos de Traveler's Titles con tipografía y animación propias, en vez del texto plano de vanilla. |
| [xali's Bushy Leaves](https://modrinth.com/resourcepack/xalis-bushy-leaves) | Hojas más frondosas y con volumen: los árboles dejan de verse planos. |

> **Fresh Animations y Better Dogs necesitan EMF + ETF**, que ya están incluidos en los mods.
> Son el reemplazo de OptiFine en Forge — sin ellos los packs se instalan pero no hacen nada.

---

## Apagar un mod sin sacarlo del pack

Agregale `.disabled` al final del nombre del archivo:

```bash
# macOS / Linux
mv mods/DistantHorizons-2.4.5-b-1.20.1-fabric-forge.jar{,.disabled}

# Windows (PowerShell)
Rename-Item mods\DistantHorizons-2.4.5-b-1.20.1-fabric-forge.jar `
            DistantHorizons-2.4.5-b-1.20.1-fabric-forge.jar.disabled
```

Forge ignora nativamente cualquier `.jar.disabled`, y `sync.py` lo respeta: no te lo
vuelve a bajar ni lo borra con `--prune`. Te lo reporta como *apagado*. Para prenderlo
de vuelta, sacale el sufijo.

> ### DH + shaders en Forge: pendiente
>
> DH funciona bien solo, y **con BSL también**. Con **Bliss** rompía el cielo y las zonas sin
> cargar, y probar DH 2.3.6 (la versión contemporánea de Bliss 2.1.2) no lo arregló, así que
> la cronología no era la causa. Bliss quedó fuera del pack por eso.
>
> El indicio bueno: la misma combinación **funciona con Iris**, el original de Fabric. Apunta
> a que el problema está en **Oculus**, el port de Iris a Forge, y no en DH ni en el shader.
>
> Si cambiás de versión de DH, puede que tengas que borrar `DistantHorizons.sqlite` de la
> carpeta del mundo — el formato no siempre es compatible hacia atrás. Se regenera solo.

**Distant Horizons** es el candidato obvio: genera terreno lejano usando el generador de
chunks del juego, y con Terralith + Incendium + los mods de estructuras eso es caro. Las
primeras horas de un mundo nuevo va a estar trabajando fuerte. Si te molesta, se apaga.

Dos formas de bajarle el volumen sin llegar a eso:

- **Desde el juego**: Opciones → Distant Horizons → *Enable Rendering*. Se apaga el
  dibujado sin tocar archivos.
- **Ajustando**: el trabajo de generación crece con el **cuadrado** del radio, así que
  bajarlo de 128 a 64 son 4 veces menos chunks. Con Terralith, Incendium y ~30 mods de
  estructuras encima, cada chunk cuesta varias veces lo que uno vanilla:

  | LOD radius | Chunks | Tiempo relativo |
  |---|---|---|
  | 128 (default) | ~51.000 | 1× |
  | **64** | ~12.900 | **4× más rápido** |
  | 48 | ~7.200 | 7× más rápido |

  Empezá con **LOD radius 64**, *Distance Generator Mode* en **5. Surface** mientras genera,
  y el render distance de Minecraft en 8–12. Se genera una sola vez por zona.

- **RAM**: 6 GB, no más. En una máquina de 16 GB, darle 9 deja al sistema sin aire y encima
  alarga las pausas del recolector de basura. Más heap no es más FPS.

---

## Shaders

| Shader | Qué es |
|---|---|
| [BSL Shaders v8.2.09](https://modrinth.com/shader/bsl-shaders) | El mejor equilibrio entre cómo se ve y cuánto cuesta, con un menú de configuración enorme para bajarle cosas si te pesa. |

Funciona gracias a **Oculus** (el port de Iris para Forge) + **Embeddium** (el port de Sodium),
que ya están en la lista de mods. Embeddium por sí solo sube los FPS aunque nunca actives un shader.

Se activa en Opciones → Video Settings → Shader Packs.

> ### ⚠️ La versión de BSL está fijada a propósito
>
> Los shaders modernos usan **compute shaders**, que necesitan **OpenGL 4.3**. macOS tope en
> **4.1** y Apple ya no lo actualiza, así que en Mac no arrancan — no importa qué GPU tengas.
>
> **BSL v8.2.09 usa cero**, así que anda en todos lados. La v10.x los agregó: actualizarla
> rompería el pack en Mac. Por lo mismo quedaron afuera **Aurora's Shaders**, **Bloop** y
> **Bliss**.
>
> Si dejás de jugar en Mac, podés subir BSL a la última cambiándole `version_number`, `url`,
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
