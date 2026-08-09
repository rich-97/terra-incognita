# Alex's Caves rompe Distant Horizons y el shader Bliss

**Estado:** Alex's Caves sacado del pack. Tiene arreglo por config, falta probarlo.

Alex's Caves resultó ser la causa de **dos** problemas que parecían no tener relación:

1. Distant Horizons generaba los LOD pero **no dibujaba nada**, con shader y sin shader.
2. El shader **Bliss** rompía el cielo y las zonas con mundo sin cargar.

Sacarlo arregló los dos de golpe. BSL nunca se vio afectado.

## Síntomas

DH generaba bien: el overlay de progreso contaba chunks y llegaba a cero. Pero no dibujaba
nada, y **ninguna opción de render tenía efecto** — ni siquiera *Debug → Only Render LODs*,
que debería ocultar el terreno vanilla y no hacía absolutamente nada. Esa fue la pista de
que el renderizador de DH ni siquiera estaba enganchado al pipeline.

## Causa

DH lo detecta solo y lo avisa por dos vías. En `logs/latest.log`:

```
[Worker-Main-2/WARN]: Partially Incompatible Distant Horizons mod detected: [Alex's Caves]
                      may require some config changes in order to render Distant Horizons correctly.
```

Y en el chat al entrar al mundo:

```
Distant Horizons: Alex's Cave detected. You may have to change Alex's config for DH to render.
```

El conflicto está en `com/github/alexmodguy/alexscaves/mixin/client/LightTextureMixin`, que
sobreescribe la textura de luz del juego y consulta `ACLoadedMods.isDistantHorizonsLoaded()`
junto con un booleano de `ACClientConfig`. Los LOD se dibujaban sin iluminación válida.

Que además rompiera a Bliss encaja: Alex's Caves también trae `biomeSkyOverrides` y
`biomeSkyFogOverrides`, que pisan el cielo y la niebla por bioma. Bliss dibuja su propio
cielo y volumétricos; BSL es más conservador y por eso sobrevivía.

## Arreglo a probar

En `config/alexscaves-client.toml`, sección `[visuals]`:

```toml
biome_ambient_light = false
biome_ambient_light_coloring = false
biome_sky_overrides = false
biome_sky_fog_overrides = false
```

Los comentarios del propio mod ya avisan del riesgo:

| Opción | Comentario en el mod |
|---|---|
| `biome_ambient_light` | *true if some biomes, such as primordial caves, have ambient light that makes the biome easier to see in.* |
| `biome_ambient_light_coloring` | *true if some biomes, such as toxic caves, apply a color to ambient light. **May conflict with shaders.*** |
| `biome_sky_overrides` | *true if some biomes, such as primordial caves, have an always well-lit sky when in them. **May conflict with shaders.*** |
| `biome_sky_fog_overrides` | *true if some biomes, such as toxic caves, have an thicker fog to them. **May conflict with shaders.*** |

Empezar por las dos de `ambient_light`, que son las que toca el `LightTextureMixin`, y
después las de cielo para Bliss. Prender de a una para encontrar el conjunto mínimo.

## Costo si se aplica

Las cuevas de Alex's Caves pierden su iluminación ambiental y su cielo especial: se van a ver
más planas de lo que el autor diseñó. Hay que decidir si vale la pena frente a tener DH y
Bliss funcionando.

## Pendiente

- [ ] Probar los toggles y encontrar el conjunto mínimo
- [ ] Decidir: ¿Alex's Caves con sus efectos apagados, o sin Alex's Caves?
- [ ] Si vuelve al pack, versionar `alexscaves-client.toml` en el repo — hoy `sync.py` maneja
      mods, resource packs y shaders, pero no configs

## Detalle aparte encontrado en el mismo log

Había **dos jars de DH cargados a la vez** en `.minecraft/mods` (2.3.6 y 2.4.5). Forge tomó
el 2.4.5 e ignoró el otro, pero conviene no dejar duplicados. Pasa porque `sync.py --prune`
limpia el repo, no la carpeta de `.minecraft` a la que se copia a mano. Un `sync.py --install`
que copie a la carpeta correcta según el sistema lo evitaría.
