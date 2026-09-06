"""Leccion 5 - Colisiones y fusion.

Ahora las piezas se detienen al tocar el fondo u otra pieza y se quedan pegadas
(fusionadas) al tablero. Deja caer varias y observa como se acumulan.

    python main.py

Controles: flechas para mover/rotar/bajar, Esc para salir.
"""


def main():
    try:
        from tetris import grafico
    except ImportError:
        print("Falta Pygame. Instala las dependencias con:")
        print("    pip install -r requirements.txt")
        return

    grafico.ejecutar()


if __name__ == "__main__":
    main()
