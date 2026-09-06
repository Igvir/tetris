# Tetris con Matrices — Lección 7: Colores neón

Esta rama corresponde a la **Lección 7**. ¡El salto visual! Pasamos de dibujar
**números** a pintar cada pieza con su **color neón** sobre fondo oscuro. Lo más
importante: **la lógica no cambió**. `juego.py`, `tablero.py` y `piezas.py`
(salvo añadir el diccionario de colores) son los mismos de la lección anterior.

## Qué aprenderás
- Asociar cada número de pieza a un color neón.
- Dibujar rectángulos con contorno claro para simular el brillo.
- Comprobar el valor de separar la **lógica** de la **presentación**: cambiar el
  aspecto sin tocar las reglas del juego.

## Instalar y ejecutar

```bash
pip install -r requirements.txt
python main.py
```

Controles: ← → mover, ↑ rotar, ↓ bajar, R reiniciar (al terminar), Esc salir.

> Compara `git diff leccion-6-lineas-puntuacion leccion-7-neon`: verás que solo
> cambiaron `piezas.py` (colores) y `grafico.py` (dibujo). La lógica está intacta.

## Lecciones
- Anterior: `git checkout leccion-6-lineas-puntuacion`
- Siguiente: `git checkout leccion-8-sonidos-animaciones` (sonidos y animaciones)

La guía completa está en [docs/guia_estudiante.md](docs/guia_estudiante.md) de la rama `main`.
