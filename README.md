# Tetris con Matrices — Lección 1: La matriz y el tablero 10×20

Esta rama corresponde a la **Lección 1** del curso. Aquí todavía no hay gráficos:
el objetivo es entender que el tablero de Tetris es una **matriz** (lista de listas)
y aprender a crearlo y mostrarlo con números en la terminal.

## Qué aprenderás
- Qué es una matriz (lista de listas).
- Crear el tablero como matriz de 20 filas × 10 columnas llena de `0`.
- Leer y escribir una casilla con `tablero[fila][columna]`.

## Ejecutar

```bash
python main.py
```

Verás una cuadrícula de `0` con un `1` en dos esquinas. `0` es una casilla vacía.

> **Regla de oro del curso:** siempre `matriz[fila][columna]`. Primero la fila
> (vertical), luego la columna (horizontal).

## Siguiente lección
`git checkout leccion-2-piezas` para representar las piezas como matrices.

La guía completa está en [docs/guia_estudiante.md](docs/guia_estudiante.md) de la rama `main`.
