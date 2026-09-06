# Sonidos del juego

El juego usa estos archivos de sonido:

- `giro.wav` — sonido corto al rotar una pieza con exito.
- `linea.wav` — sonido al eliminar una o mas filas completas.

Ya vienen incluidos en el proyecto, asi que el juego suena sin que hagas nada.

## Regenerarlos o cambiarlos

Los sonidos se generaron con Python puro (sin descargar nada). Puedes volver a
crearlos con:

```bash
python tools/generar_sonidos.py
```

Tambien puedes reemplazarlos por cualquier archivo `.wav` corto y ligero;
solo respeta los nombres `giro.wav` y `linea.wav`.

## Nota

Los sonidos son **opcionales**: si borras estos archivos, el juego seguira
funcionando, simplemente sin audio (degradacion segura).
