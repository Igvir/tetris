"""Logica del juego: la pieza activa, su movimiento y el estado global.

PLANTILLA DE INICIO: completa la clase Juego siguiendo la guia del estudiante
(Lecciones 4, 5 y 6). Esta clase solo manipula matrices de numeros: no sabe nada
de graficos ni de sonido, por eso se reutiliza sin cambios entre el estilo
numeros y el estilo neon.
"""

from . import piezas
from . import tablero as tab

# Puntos segun cuantas lineas se eliminan a la vez (Leccion 6).
PUNTOS_POR_LINEAS = {0: 0, 1: 100, 2: 300, 3: 500, 4: 800}


class Juego:
    """Mantiene el estado del juego y aplica las reglas sobre las matrices.

    TODO (Lecciones 4-6): implementa el estado y los metodos de abajo.
    """

    def __init__(self):
        self.tablero = tab.crear_tablero()
        self.puntuacion = 0
        self.lineas = 0
        self.terminado = False
        self.pieza = None
        self.rotacion = 0
        self.fila = 0
        self.columna = 0
        self.nueva_pieza()

    def matriz_pieza_actual(self):
        """Devuelve la matriz de la rotacion actual de la pieza activa."""
        return piezas.PIEZAS[self.pieza][self.rotacion]

    def nueva_pieza(self):
        """Genera una pieza nueva arriba y al centro. Si no cabe, fin del juego.

        TODO (Lecciones 4 y 6): elige una pieza al azar, ponla en la fila 0 y
        centrada; en la Leccion 6, marca `terminado` si no cabe.
        """
        # TODO: reemplaza esto por tu implementacion.
        raise NotImplementedError("Completa nueva_pieza en las Lecciones 4 y 6")

    def mover(self, dx):
        """Mueve la pieza dx columnas (-1 izquierda, +1 derecha) si es valido.

        TODO (Leccion 4): aplica el movimiento solo si es_valida lo permite.
        """
        # TODO: reemplaza esto por tu implementacion.
        raise NotImplementedError("Completa mover en la Leccion 4")

    def rotar(self):
        """Pasa a la siguiente rotacion (ciclica) solo si la nueva cabe.

        TODO (Leccion 4): usa el operador modulo para la rotacion ciclica y
        aplicala solo si es_valida lo permite.
        """
        # TODO: reemplaza esto por tu implementacion.
        raise NotImplementedError("Completa rotar en la Leccion 4")

    def bajar(self):
        """Baja una fila. Si no puede, fusiona, elimina lineas y saca pieza nueva.

        TODO (Lecciones 4-6): baja si se puede; si no, fusiona (Leccion 5),
        elimina lineas y suma puntos (Leccion 6) y genera una pieza nueva.
        Devuelve (fusiono, lineas_eliminadas) para que la presentacion pueda
        disparar sonidos y animaciones.
        """
        # TODO: reemplaza esto por tu implementacion.
        raise NotImplementedError("Completa bajar en las Lecciones 4, 5 y 6")

    def caida_rapida(self):
        """Baja la pieza hasta el fondo de una sola vez y la fusiona.

        TODO (opcional / reto): baja mientras sea valido y luego llama a bajar().
        """
        # TODO: reemplaza esto por tu implementacion.
        raise NotImplementedError("Completa caida_rapida (opcional)")

    def tablero_con_pieza(self):
        """Devuelve una COPIA del tablero con la pieza activa dibujada.

        TODO (Leccion 4): copia el tablero y dibuja encima la pieza activa, sin
        modificar el tablero real.
        """
        # TODO: reemplaza esto por tu implementacion.
        raise NotImplementedError("Completa tablero_con_pieza en la Leccion 4")

    def celdas_pieza_actual(self):
        """Lista de (fila, columna) ocupadas por la pieza activa en el tablero.

        TODO (Leccion 8): util para la animacion de destello al fusionar.
        """
        # TODO: reemplaza esto por tu implementacion.
        raise NotImplementedError("Completa celdas_pieza_actual en la Leccion 8")

    def reiniciar(self):
        """Reinicia el juego a su estado inicial."""
        self.__init__()
