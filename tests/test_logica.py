"""Pruebas de la logica de matrices del Tetris.

Se centran en la logica pura (sin graficos ni sonido): crear el tablero,
validar posiciones, fusionar, eliminar lineas y rotar de forma ciclica.
"""

import os
import sys

# Permite importar el paquete `tetris` al ejecutar pytest desde la raiz.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tetris import tablero as tab
from tetris import piezas
from tetris.juego import Juego


def test_crear_tablero_dimensiones_y_ceros():
    t = tab.crear_tablero()
    assert len(t) == tab.ALTO
    assert all(len(fila) == tab.ANCHO for fila in t)
    assert all(celda == 0 for fila in t for celda in fila)


def test_fusionar_copia_solo_ocupadas():
    t = tab.crear_tablero()
    matriz = [[0, 3, 0],
              [3, 3, 3],
              [0, 0, 0]]
    tab.fusionar(t, matriz, 0, 0)
    assert t[0][1] == 3
    assert t[1][0] == 3 and t[1][1] == 3 and t[1][2] == 3
    # Los ceros de la pieza no deben sobrescribir el tablero.
    assert t[0][0] == 0
    assert t[2][0] == 0


def test_es_valida_fuera_de_limites():
    t = tab.crear_tablero()
    matriz = [[1, 1, 1, 1]]
    # Pegada a la izquierda es valida.
    assert tab.es_valida(t, matriz, 0, 0) is True
    # Se sale por la derecha.
    assert tab.es_valida(t, matriz, 0, tab.ANCHO - 2) is False
    # Se sale por debajo.
    assert tab.es_valida(t, matriz, tab.ALTO, 0) is False


def test_es_valida_choca_con_ocupada():
    t = tab.crear_tablero()
    t[5][3] = 2
    matriz = [[1]]
    assert tab.es_valida(t, matriz, 5, 3) is False
    assert tab.es_valida(t, matriz, 4, 3) is True


def test_eliminar_lineas_completa():
    t = tab.crear_tablero()
    # Llenamos por completo la ultima fila.
    t[tab.ALTO - 1] = [1] * tab.ANCHO
    eliminadas = tab.eliminar_lineas(t)
    assert eliminadas == 1
    # El tablero mantiene sus dimensiones y queda vacio.
    assert len(t) == tab.ALTO
    assert all(len(fila) == tab.ANCHO for fila in t)
    assert all(celda == 0 for fila in t for celda in fila)


def test_eliminar_lineas_desplaza_hacia_abajo():
    t = tab.crear_tablero()
    # Fila con un hueco (no se elimina) encima de una fila completa.
    t[tab.ALTO - 2][0] = 6
    t[tab.ALTO - 1] = [1] * tab.ANCHO
    eliminadas = tab.eliminar_lineas(t)
    assert eliminadas == 1
    # El bloque de la fila incompleta baja a la ultima fila.
    assert t[tab.ALTO - 1][0] == 6


def test_lineas_completas_indices():
    t = tab.crear_tablero()
    t[0] = [1] * tab.ANCHO
    t[tab.ALTO - 1] = [1] * tab.ANCHO
    assert tab.lineas_completas(t) == [0, tab.ALTO - 1]


def test_rotacion_ciclica():
    juego = Juego()
    juego.tablero = tab.crear_tablero()
    juego.pieza = "T"
    juego.rotacion = 0
    juego.fila = 0
    juego.columna = 3
    total = len(piezas.PIEZAS["T"])
    for _ in range(total):
        juego.rotar()
    # Tras dar la vuelta completa, volvemos a la rotacion inicial.
    assert juego.rotacion == 0


def test_rotar_solo_cambia_de_matriz():
    # Cada estado de rotacion es una matriz predefinida en PIEZAS.
    for nombre, estados in piezas.PIEZAS.items():
        for matriz in estados:
            # Todos los numeros no nulos coinciden con el numero de la pieza.
            numero = piezas.NUMERO_PIEZA[nombre]
            for fila in matriz:
                for celda in fila:
                    assert celda in (0, numero)
