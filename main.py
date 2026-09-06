"""Leccion 4 - La pieza que cae.

Una pieza baja sola por el tablero. Muevela con las flechas izquierda/derecha,
rotala con la flecha arriba y acelerala con la flecha abajo. Por ahora, al
llegar al fondo la pieza reaparece arriba (aun no se acumula).

    python main.py

Cierra la ventana o pulsa Esc para salir.
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
