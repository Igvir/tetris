"""Punto de entrada del juego Tetris con Matrices.

Abre la ventana de Pygame y ejecuta el juego. Por defecto usa el estilo neon;
puedes pasar "numeros" como argumento para ver la version que dibuja los
numeros de las matrices (Etapa 1 del tutorial):

    python main.py            # estilo neon
    python main.py numeros    # estilo numeros
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

    jugar(estilo=estilo)


if __name__ == "__main__":
    main()
