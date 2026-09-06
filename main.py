"""Punto de entrada del juego Tetris con Matrices (plantilla de inicio).

Esta es la rama `inicio`: los modulos del juego estan como esqueleto con TODOs.
A medida que completes las lecciones, este archivo abrira tu juego:

    python main.py            # estilo neon
    python main.py numeros    # estilo numeros

Mientras haya partes sin implementar, veras un mensaje indicando que aun falta
completar codigo (es normal al empezar el curso).
"""

import sys


def main():
    try:
        from tetris.grafico import jugar, ESTILO_NUMEROS, ESTILO_NEON
    except ImportError:
        print("Falta Pygame. Instala las dependencias con:")
        print("    pip install -r requirements.txt")
        return

    estilo = ESTILO_NEON
    if len(sys.argv) > 1 and sys.argv[1].lower() == "numeros":
        estilo = ESTILO_NUMEROS

    try:
        jugar(estilo=estilo)
    except NotImplementedError as e:
        print("Aun falta completar codigo del juego:")
        print("   ->", e)
        print("Sigue la guia del estudiante en docs/ para implementarlo.")


if __name__ == "__main__":
    main()
