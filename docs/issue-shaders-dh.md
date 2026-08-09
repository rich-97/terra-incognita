# Bliss + Distant Horizons: resuelto, y qué se descartó en el camino

**Estado:** resuelto. La causa era Alex's Caves, no el shader ni DH ni Oculus.
Bliss volvió al pack. Este documento existe para no repetir los callejones sin salida.

## Qué pasaba

Con Bliss + DH en Windows: el cielo se rompía y las zonas con mundo sin cargar se veían
visualmente corruptas. BSL funcionaba bien en la misma máquina con el mismo DH.

**Causa real: Alex's Caves.** Ver `issue-alexs-caves.md`. Al sacarlo, Bliss quedó perfecto
sin tocar nada más.

## Hipótesis descartadas — no volver a probarlas

- **Desfase de versiones DH ↔ Bliss.** Bliss 2.1.2 salió el 2025-11-23 y la rama DH 2.4 el
  2025-12-13, así que parecía que Bliss nunca se había probado contra ella. Se fijó
  **DH 2.3.6** (2025-10-13, el DH vigente cuando salió Bliss) y **no cambió nada**.
- **`Overdraw prevention` de Bliss**, en *Mod support → Distant Horizons*. Se ajustó de
  *Unlimited* a valores finitos, sin efecto.
- **Bliss desactiva su código DH si no detecta Iris.** Su menú se llama
  *"Distant Horizons — IRIS REQUIRED"*, así que parecía que en Forge no se activaba. Falso:
  Oculus **sí** inyecta los macros `IS_IRIS` y `DISTANT_HORIZONS` — verificado en
  `net/irisshaders/iris/gl/shader/StandardMacros.class` dentro del jar de Oculus.
- **Comparar los uniforms `dh*` de cada shader.** Bliss usa `dhDepthOpaque` y `dhDepthOpaqueL`,
  que BSL no. Pero el método no sirve: extrayendo strings del jar de Oculus, `dhProjection` y
  `dhMaterialId` también parecen "ausentes" y BSL los usa sin problema. Oculus arma esos
  nombres en runtime, así que no se pueden ver así.
- **Embeddium.** Sospechado porque DH del lado Forge solo trae `OculusAccessor` y
  `OptifineAccessor`, sin accessor de Sodium/Embeddium (ese existe solo en el paquete
  `fabric/`). Nunca se llegó a probar el A/B porque apareció la causa real.

## Lo que sí quedó como nota real

DH avisa al arrancar, en `logs/latest.log`:

```
[Worker-Main-2/WARN]: Partial Oculus support enabled. Some DH features may be
                      disabled or behave strangely, use Iris instead if possible.
```

El soporte de DH en Forge es parcial por diseño, y Oculus está **congelado en 1.20.1-1.8.0
desde diciembre de 2024** mientras DH sigue publicando. No causó este problema, pero es deuda
latente: si aparecen rarezas futuras entre DH y shaders, este es el sospechoso.

## Migrar a Fabric + Iris: medido, y por ahora innecesario

Se evaluó porque Iris es el original y Oculus el port. Con el problema resuelto **ya no hace
falta**, pero queda el número por si el tema vuelve.

Contra la API de Modrinth, sobre los mods del pack consultables ahí:

| | |
|---|---|
| Con build de Fabric 1.20.1 | **83** |
| Sin build de Fabric 1.20.1 | **23** |

(Más 6 mods que solo están en CurseForge y no se pudieron verificar por API.)

Los 23 sin Fabric:

```
Alex's Mobs · Apothic Attributes · Bosses of Mass Destruction · Citadel
CodeChicken Lib · Corpse · Ender Storage · Enhanced Boss Bars
Falling Leaves · ForgeEndertech · Friends&Foes · Gateways to Eternity
Ice and Fire · It Takes a Pillage · Large Ore Deposits · Oculus
Placebo · Sophisticated Backpacks · Sophisticated Core · Spartan Weaponry
The Bumblezone · The Graveyard · XP Tome
```

**La lista está inflada.** Varios son proyectos con nombre "Forge/NeoForge" que tienen un
proyecto hermano para Fabric, publicado aparte: *Friends&Foes*, *The Bumblezone*,
*The Graveyard*, *Falling Leaves*. Y *Oculus* se reemplaza por **Iris**, que sería el objetivo.

**Los que se pierden de verdad:** `Ice and Fire`, `Alex's Mobs` y `Citadel` son del mismo
autor y solo existen en Forge. Ice and Fire es una de las razones por las que este pack vive
en 1.20.1 — ver el análisis de versiones en el README. `Sophisticated Backpacks`,
`Spartan Weaponry`, `Gateways to Eternity` y `Placebo`/`Apothic` tampoco tienen Fabric.

## Lección del episodio

Los dos síntomas parecían de dominios distintos —uno de renderizado de terreno, otro de
cielo en un shader— y eran el mismo mod. La pista que resolvió todo no salió de comparar
shaders ni versiones: salió de **leer el log**, donde DH nombraba al culpable en texto plano
desde el primer arranque.
