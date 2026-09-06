"""Definicion de las piezas (tetrominos) como matrices.

PLANTILLA DE INICIO: completa PIEZAS y las funciones marcadas con TODO siguiendo
la guia del estudiante (Lecciones 2 y 7). Cada pieza es una MATRIZ donde `0` es
una casilla vacia y un numero del 1 al 7 identifica la pieza. La rotacion NO se
calcula: cada pieza guarda una lista con todas sus matrices de rotacion.
"""

import random

# Numero identificador de cada pieza. El numero tambien decide su color neon.
NUMERO_PIEZA = {
    "I": 1,
    "O": 2,
    "T": 3,
    "S": 4,
    "Z": 5,
    "J": 6,
    "L": 7,
}

# Colores neon por numero de pieza (se usan en la Leccion 7, estilo neon).
# TODO (Leccion 7): completa el color de cada pieza segun la tabla de la guia.
COLORES = {
    0: (10, 10, 20),      # fondo oscuro (casilla vacia)
    # 1: (0, 255, 255),   # I - cian neon
    # 2: (255, 255, 0),   # O - amarillo neon
    # ... completa del 1 al 7 en la Leccion 7.
}

# Cada pieza es una lista de matrices de rotacion. Rotar = pasar a la siguiente.
# TODO (Leccion 2): completa TODAS las piezas (I, O, T, S, Z, J, L) con sus
# matrices de rotacion. Se deja la T como ejemplo ya resuelto para guiarte.
PIEZAS = {
    "T": [
        [[0, 3, 0],
         [3, 3, 3],
         [0, 0, 0]],
        [[0, 3, 0],
         [0, 3, 3],
         [0, 3, 0]],
        [[0, 0, 0],
         [3, 3, 3],
         [0, 3, 0]],
        [[0, 3, 0],
         [3, 3, 0],
         [0, 3, 0]],
    ],
    # TODO: agrega "I", "O", "S", "Z", "J", "L" con sus rotaciones.
}


def pieza_aleatoria():
    """Devuelve el nombre de una pieza elegida al azar.

    TODO (Leccion 2): devuelve un nombre al azar de las claves de PIEZAS.
    """
    # TODO: reemplaza esto por tu implementacion.
    raise NotImplementedError("Completa pieza_aleatoria en la Leccion 2")


def mostrar_pieza(nombre, rotacion=0):
    """Imprime en la terminal la matriz de una pieza (util para depurar)."""
    matriz = PIEZAS[nombre][rotacion]
    for fila in matriz:
        print(" ".join(str(celda) for celda in fila))
