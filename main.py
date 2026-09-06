"""Leccion 2 - Las piezas y sus rotaciones.

Seguimos en la terminal. Aqui vemos que cada pieza es una matriz de numeros y
que rotar es simplemente cambiar de matriz. Ejecuta:

    python main.py
"""

from tetris.piezas import PIEZAS, mostrar_pieza


def main():
    print("La pieza T (numero 3) y sus 4 rotaciones:\n")
    for indice in range(len(PIEZAS["T"])):
        print(f"Rotacion {indice}:")
        mostrar_pieza("T", indice)
        print()

    print("La pieza I (numero 1) tiene 2 rotaciones (horizontal y vertical):\n")
    for indice in range(len(PIEZAS["I"])):
        print(f"Rotacion {indice}:")
        mostrar_pieza("I", indice)
        print()

    print("La pieza O (numero 2) es un cuadrado: una sola rotacion.\n")
    mostrar_pieza("O", 0)


if __name__ == "__main__":
    main()
