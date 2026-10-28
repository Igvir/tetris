"""Definicion de las piezas (tetrominos) como matrices.

La idea central del curso: cada pieza es una MATRIZ (lista de listas) donde
`0` es una casilla vacia y un numero del 1 al 7 identifica la pieza. La
rotacion NO se calcula: cada pieza guarda una lista con todas sus matrices de
rotacion ya escritas y rotar significa pasar a la siguiente matriz.
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

# Colores neon por numero de pieza (usados en la Etapa 2, estilo neon).
COLORES = {
    0: (10, 10, 20),      # fondo oscuro (casilla vacia)
    1: (0, 255, 255),     # I - cian neon
    2: (255, 255, 0),     # O - amarillo neon
    3: (255, 0, 255),     # T - magenta neon
    4: (57, 255, 20),     # S - verde neon
    5: (255, 49, 49),     # Z - rojo/rosa neon
    6: (77, 77, 255),     # J - azul neon
    7: (255, 149, 0),     # L - naranja neon
}

# Cada pieza es una lista de matrices de rotacion. Rotar = pasar a la
# siguiente matriz de la lista (de forma ciclica).
PIEZAS = {
    "I": [
        [[0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        [[0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0]],
    ],
    "O": [
        [[2, 2],
         [2, 2]],
    ],
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
    "S": [
        [[0, 4, 4],
         [4, 4, 0],
         [0, 0, 0]],
        [[0, 4, 0],
         [0, 4, 4],
         [0, 0, 4]],
    ],
    "Z": [
        [[5, 5, 0],
         [0, 5, 5],
         [0, 0, 0]],
        [[0, 0, 5],
         [0, 5, 5],
         [0, 5, 0]],
    ],
    "J": [
        [[6, 0, 0],
         [6, 6, 6],
         [0, 0, 0]],
        [[0, 6, 6],
         [0, 6, 0],
         [0, 6, 0]],
        [[0, 0, 0],
         [6, 6, 6],
         [0, 0, 6]],
        [[0, 6, 0],
         [0, 6, 0],
         [6, 6, 0]],
    ],
    "L": [
        [[0, 0, 7],
         [7, 7, 7],
         [0, 0, 0]],
        [[0, 7, 0],
         [0, 7, 0],
         [0, 7, 7]],
        [[0, 0, 0],
         [7, 7, 7],
         [7, 0, 0]],
        [[7, 7, 0],
         [0, 7, 0],
         [0, 7, 0]],
    ],
}


def pieza_aleatoria():
    """Devuelve el nombre de una pieza elegida al azar.

    [SEGURIDAD - azar "de juego" vs. azar "criptografico"]
    El modulo `random` es rapido y perfecto para juegos, pero NO es apto para
    cosas sensibles (contrasenas, tokens, sorteos con dinero), porque su
    secuencia es predecible si alguien conoce la semilla. La herramienta de
    analisis de seguridad `bandit` marca cualquier uso de `random` con el aviso
    B311 por si acaso.

    Aqui es un falso positivo: elegir la proxima pieza es puro juego, no hay
    nada que proteger. Por eso anadimos el comentario `# nosec B311`, que le
    dice a bandit "esto ya lo revisamos y es seguro". Si algun dia necesitaras
    azar de verdad impredecible, usarias el modulo `secrets` en su lugar.
    """
    return random.choice(list(PIEZAS.keys()))  # nosec B311


def mostrar_pieza(nombre, rotacion=0):
    """Imprime en la terminal la matriz de una pieza (util para depurar)."""
    matriz = PIEZAS[nombre][rotacion]
    for fila in matriz:
        print(" ".join(str(celda) for celda in fila))
