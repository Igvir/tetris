# Tetris con Matrices — Lección 4: La pieza que cae

Esta rama corresponde a la **Lección 4**. Creamos la clase `Juego` para guardar
el estado de la pieza activa. Ahora una pieza **cae sola** y puedes moverla y
rotarla. Seguimos viendo la matriz con **números**.

## Qué aprenderás
- Guardar el estado de la pieza (nombre, rotación, fila, columna) en una clase.
- Mover la pieza a los lados, rotarla (cambiando de matriz) y hacerla bajar.
- El bucle de juego y la caída automática por tiempo.

## Instalar y ejecutar

```bash
pip install -r requirements.txt
python main.py
```

Controles: ← → mover, ↑ rotar, ↓ bajar más rápido, Esc salir.

> Nota: en esta lección, al llegar al fondo la pieza **reaparece arriba** sin
> acumularse. La acumulación (fusión) llega en la Lección 5.

## Lecciones
- Anterior: `git checkout leccion-3-ventana-numeros`
- Siguiente: `git checkout leccion-5-colisiones-fusion` (las piezas se acumulan)

La guía completa está en [docs/guia_estudiante.md](docs/guia_estudiante.md) de la rama `main`.
