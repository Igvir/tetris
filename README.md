# Tetris con Matrices — Lección 5: Colisiones y fusión

Esta rama corresponde a la **Lección 5**. Ahora las piezas **se detienen** al
tocar el fondo u otra pieza y se quedan pegadas: su matriz se **fusiona** con la
del tablero. Las piezas se acumulan como en el Tetris clásico. Seguimos en modo
**números**.

## Qué aprenderás
- Detectar colisiones con `es_valida` (límites y casillas ocupadas).
- Fusionar la matriz de la pieza dentro del tablero al aterrizar.
- Recorrer solo las casillas ocupadas (`!= 0`) de la pieza.

## Instalar y ejecutar

```bash
pip install -r requirements.txt
python main.py
```

Deja caer varias piezas y observa cómo se acumulan sin borrarse entre sí.

## Lecciones
- Anterior: `git checkout leccion-4-pieza-cae`
- Siguiente: `git checkout leccion-6-lineas-puntuacion` (líneas, puntos y fin del juego)

La guía completa está en [docs/guia_estudiante.md](docs/guia_estudiante.md) de la rama `main`.
