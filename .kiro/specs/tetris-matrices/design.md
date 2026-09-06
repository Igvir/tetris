# Diseño - Tetris con Matrices

## Visión general

El proyecto implementa un Tetris en Python con un objetivo pedagógico: enseñar el uso de **matrices (listas de listas)**. Se separa deliberadamente la **lógica del juego** (que solo manipula matrices de números) de la **capa de presentación** (que siempre dibuja en una ventana de **Pygame**).

La presentación evoluciona en dos estilos sobre la misma ventana gráfica:

- **Etapa 1 (números):** la ventana dibuja el número de cada casilla como texto sobre la cuadrícula.
- **Etapa 2 (colores neón):** la ventana pinta cada casilla ocupada con un color neón brillante sobre fondo oscuro.

Esta separación es la clave del tutorial: la misma lógica de matrices se reutiliza en ambos estilos. El estudiante primero entiende los datos (los ve como números en la ventana) y luego solo mejora la capa de dibujo hasta el estilo neón.

```
+-----------------------------------+
|   Presentación (Pygame)           |
|   - Estilo números  (Etapa 1)     |
|   - Estilo neón     (Etapa 2)     |
+------------------+----------------+
                   | usa
                   v
+-----------------------------------+
|   Lógica del juego                 |
|   - Tablero (matriz 10x20)         |
|   - Piezas (matrices)              |
|   - Colisiones / fusión            |
|   - Rotación por matrices          |
|   - Líneas / puntuación            |
+-----------------------------------+
```

## Concepto central: todo es una matriz

### Tablero

El tablero es una lista de 20 listas, cada una con 10 enteros. `0` = vacío. Un número del 1 al 7 = casilla ocupada por una pieza de ese tipo.

```python
ANCHO = 10   # columnas
ALTO  = 20   # filas

# Tablero vacío: 20 filas, cada una con 10 ceros
tablero = [[0 for _ in range(ANCHO)] for _ in range(ALTO)]
```

Convención de coordenadas: `tablero[fila][columna]`, donde `fila` crece hacia abajo (fila 0 arriba, fila 19 abajo) y `columna` crece hacia la derecha.

### Piezas (tetrominós)

Cada pieza es una matriz pequeña. El número que la rellena la identifica y, más adelante, determina su color.

| Pieza | Número | Color neón (Etapa 2) | RGB aprox.        |
|-------|--------|----------------------|-------------------|
| I     | 1      | Cian neón            | (0, 255, 255)     |
| O     | 2      | Amarillo neón        | (255, 255, 0)     |
| T     | 3      | Magenta / morado neón| (255, 0, 255)     |
| S     | 4      | Verde neón           | (57, 255, 20)     |
| Z     | 5      | Rojo/rosa neón       | (255, 49, 49)     |
| J     | 6      | Azul neón            | (77, 77, 255)     |
| L     | 7      | Naranja neón         | (255, 149, 0)     |

El estilo neón se consigue con un fondo muy oscuro (por ejemplo `(10, 10, 20)`), colores saturados y un contorno/brillo más claro alrededor de cada celda para simular el resplandor.

Ejemplo de la pieza T (número 3) en su primer estado:

```python
[
    [0, 3, 0],
    [3, 3, 3],
    [0, 0, 0],
]
```

## Rotación por matrices alternativas

En lugar de rotar con matemáticas, **cada pieza guarda una lista con todas sus rotaciones ya escritas**. Rotar = avanzar al siguiente índice de esa lista (de forma cíclica).

```python
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
    # ... resto de piezas
}
```

Esto refuerza el mensaje del curso: **una decisión de diseño con datos puede evitar cálculos complejos**. La pieza O tiene una sola rotación; I, S, Z tienen dos; T, J, L tienen cuatro (se pueden definir las cuatro por simplicidad y consistencia).

## Componentes y estructura de archivos

El código se organiza para que la lógica sea reutilizable entre etapas.

```
tetris/
├── tetris/
│   ├── __init__.py
│   ├── piezas.py         # Matrices de cada pieza, sus rotaciones y los colores neón
│   ├── tablero.py        # Matriz del tablero: crear, fusionar, líneas
│   ├── juego.py          # Lógica del juego: pieza activa, movimiento, colisión, puntuación
│   ├── grafico.py        # Presentación en Pygame (estilo números y estilo neón)
│   └── audio.py          # Carga y reproducción de sonidos (giro, línea) con pygame.mixer
├── assets/
│   └── sonidos/          # Archivos de sonido sencillos (giro.wav, linea.wav, ...)
├── main.py               # Punto de entrada: abre la ventana de Pygame y ejecuta el juego
├── tests/                # Pruebas de la lógica de matrices
├── docs/
│   ├── guia_estudiante.md            # Curso paso a paso (con Kiro)
│   ├── guia_estudiante_sin_kiro.md   # Curso paso a paso (sin agente, a mano)
│   └── guia_instructor.md            # Guía docente: planificación, evaluación y soluciones
├── requirements.txt
└── README.md
```

Toda la presentación vive en `grafico.py` sobre una ventana de Pygame. El estilo de dibujo (números o neón) se controla dentro de ese módulo, de modo que la lógica (`piezas.py`, `tablero.py`, `juego.py`) nunca cambia entre etapas, tal como pide el Requisito 10.4.

## Modelo de datos y responsabilidades

### `piezas.py`

- `PIEZAS`: diccionario `nombre -> lista de matrices de rotación`.
- `NUMERO_PIEZA`: diccionario `nombre -> número identificador` (I=1 ... L=7).
- `COLORES`: diccionario `número -> color RGB neón` (usado en el estilo neón, Etapa 2).
- `pieza_aleatoria()`: devuelve el nombre de una pieza al azar.

### `tablero.py`

- `crear_tablero(ancho=10, alto=20)`: devuelve la matriz de ceros.
- `fusionar(tablero, matriz_pieza, fila, columna)`: copia los números distintos de `0` de la matriz de la pieza en el tablero.
- `lineas_completas(tablero)`: devuelve los índices de filas totalmente ocupadas.
- `eliminar_lineas(tablero)`: elimina filas completas, desplaza hacia abajo, añade filas vacías arriba y devuelve cuántas eliminó.
- `mostrar_tablero(tablero)` (opcional, para depurar): imprime la matriz con números en la terminal.

### `juego.py`

Clase `Juego` que mantiene el estado:

- `tablero`: matriz del tablero.
- `pieza`: nombre de la pieza activa.
- `rotacion`: índice de rotación actual.
- `fila`, `columna`: posición de la esquina superior izquierda de la matriz de la pieza dentro del tablero.
- `puntuacion`, `terminado`.

Métodos:

- `matriz_pieza_actual()`: devuelve la matriz de la rotación actual.
- `es_valida(matriz, fila, columna)`: verifica que ninguna casilla ocupada de la pieza salga del tablero ni pise una casilla ocupada.
- `mover(dx)`: mueve horizontalmente si es válido.
- `bajar()`: baja una fila; si no puede, fusiona, elimina líneas, suma puntos y genera nueva pieza.
- `rotar()`: prueba la siguiente rotación; la aplica solo si es válida.
- `nueva_pieza()`: genera pieza aleatoria en la parte superior; si no cabe, marca `terminado`.
- `tablero_con_pieza()`: devuelve una copia del tablero con la pieza activa dibujada (para presentación).

### `grafico.py` (presentación en Pygame, ambas etapas)

- Inicializa Pygame, la ventana y el reloj; contiene el bucle de juego y la lectura de teclado (mover, rotar, bajar).
- Recorre la matriz `tablero_con_pieza()` y dibuja cada celda. El **estilo** de dibujo determina la etapa:
  - `dibujar_celda_numero(...)` (Etapa 1): dibuja el número como texto sobre la cuadrícula; `0` se ve como celda vacía.
  - `dibujar_celda_neon(...)` (Etapa 2): pinta un rectángulo con `COLORES[numero]`, fondo oscuro para `0` y un contorno claro para simular el brillo neón.
- Muestra la puntuación en pantalla.
- Reutiliza la clase `Juego` sin cambios en ambos estilos.
- La evolución de Etapa 1 a Etapa 2 consiste en cambiar la función de dibujo de celda, sin tocar la lógica.
- Gestiona las **animaciones** breves de presentación (destello al fusionar y parpadeo de filas antes de eliminarse), controladas por un contador de fotogramas para no bloquear el bucle.
- Reproduce los sonidos llamando a `audio.py` en los eventos de giro y de línea eliminada.

### `audio.py` (sonidos, capa de presentación)

- `iniciar_audio()`: inicializa `pygame.mixer` de forma segura; si falla, deja el audio desactivado sin romper el juego.
- `cargar_sonidos()`: carga los archivos de `assets/sonidos/` (por ejemplo `giro.wav`, `linea.wav`) y los guarda en un diccionario.
- `reproducir(nombre)`: reproduce un sonido si el audio está disponible; si no, no hace nada (degradación silenciosa).
- Todo el audio es **opcional**: si no hay archivos o el mezclador no arranca, el juego continúa normalmente (Requisito 9b.6).

## Algoritmos clave

### Validación de posición (colisiones)

Recorre solo las casillas ocupadas de la matriz de la pieza:

```python
def es_valida(tablero, matriz, fila, columna):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                f = fila + i
                c = columna + j
                # Fuera de los límites
                if c < 0 or c >= ANCHO or f >= ALTO:
                    return False
                # Choca con casilla ocupada (ignora filas negativas: aún entrando)
                if f >= 0 and tablero[f][c] != 0:
                    return False
    return True
```

### Fusión de la pieza en el tablero

```python
def fusionar(tablero, matriz, fila, columna):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                tablero[fila + i][columna + j] = matriz[i][j]
```

### Bajar / detección de aterrizaje

```python
def bajar(self):
    if es_valida(self.tablero, self.matriz_pieza_actual(), self.fila + 1, self.columna):
        self.fila += 1
    else:
        fusionar(self.tablero, self.matriz_pieza_actual(), self.fila, self.columna)
        eliminadas = eliminar_lineas(self.tablero)
        self.puntuacion += self.puntos(eliminadas)
        self.nueva_pieza()
```

### Eliminación de líneas

```python
def eliminar_lineas(tablero):
    filas_restantes = [fila for fila in tablero if 0 in fila]
    eliminadas = ALTO - len(filas_restantes)
    nuevas = [[0] * ANCHO for _ in range(eliminadas)]
    tablero[:] = nuevas + filas_restantes
    return eliminadas
```

## Manejo de errores

- Movimientos y rotaciones inválidos se rechazan silenciosamente (no lanzan error): el estado simplemente no cambia.
- La entrada del teclado no reconocida se ignora.
- Cerrar la ventana termina el bucle limpiamente (`pygame.quit()`).
- Si Pygame no está instalado, `main.py` muestra un mensaje claro pidiendo `pip install -r requirements.txt`.
- El audio es opcional: si `pygame.mixer` no se inicializa o falta un archivo de sonido, el juego continúa sin audio y sin lanzar error (Requisito 9b.6).
- Las animaciones se controlan por un contador de fotogramas y duran pocos frames, de modo que no bloquean el bucle de juego (Requisito 9b.7).

## Estrategia de pruebas

Las pruebas se centran en la lógica de matrices (sin gráficos), en la línea del `test_snake.py` del curso anterior:

- Crear tablero con las dimensiones correctas y todo en `0`.
- Fusionar una pieza copia los números en las posiciones esperadas.
- `es_valida` rechaza posiciones fuera de límites y sobre casillas ocupadas.
- `eliminar_lineas` elimina filas completas, desplaza correctamente y cuenta las eliminadas.
- Rotar es cíclico y solo cambia de matriz.

Ejecución sugerida: `python -m pytest tests/`.

## Documentación del curso

El proyecto es un tutorial, por lo que la documentación es un entregable de primer nivel. Se organiza en tres piezas complementarias, todas en español.

### `README.md`

Puerta de entrada del repositorio: descripción, objetivos de aprendizaje, requisitos (Python + Pygame), instalación, cómo ejecutar el juego y un índice que enlaza a las guías de `docs/`.

Incluye además una sección **"Entrega de la asignación"** con el flujo de Git que debe seguir el estudiante, en la línea de la "Guía GIT" del curso Snake:

1. Clonar (o hacer fork de) el repositorio.
2. Crear una rama con su nombre a partir de la plantilla `inicio`, por ejemplo `git checkout -b tetris-juan-perez origin/inicio`.
3. Trabajar en su solución y confirmar los cambios.
4. Subir la rama con `git push -u origin <rama>`.
5. Abrir un **Pull Request** hacia la rama principal.

Se explica que el Pull Request es la **evidencia de que completó la asignación**. Ejemplo de comandos:

```bash
git clone <url-del-repositorio>
cd tetris
git checkout -b tetris-nombre-apellido origin/inicio
# ... trabajar y guardar cambios ...
git add .
git commit -m "Completa la asignacion de Tetris"
git push -u origin tetris-nombre-apellido
# Abrir el Pull Request desde la interfaz de GitHub
```

### Dos rutas para el estudiante

El curso ofrece **dos guías del estudiante** con la misma progresión de 8
lecciones y el mismo juego final; el estudiante elige una:

- **Con Kiro** (`guia_estudiante.md`): construye el juego con ayuda de un
  asistente y *spec driven development*, escribiendo prompts.
- **Sin Kiro** (`guia_estudiante_sin_kiro.md`): aprende a programar escribiendo
  todo el código a mano, sin ningún agente de IA.

Ambas guías se enlazan mutuamente y comparten mapeo de piezas, colores neón,
algoritmos y las ramas de Git por lección. La única diferencia es el **método de
trabajo**: prompts frente a escritura manual y depuración autónoma.

### `docs/guia_estudiante.md` (con Kiro)

Curso paso a paso, estructurado en **lecciones/sesiones** que siguen las etapas del proyecto. Cada lección incluye:

- Objetivos de aprendizaje y conceptos nuevos.
- Explicación del concepto de **matrices** aplicado a esa etapa (tablero, piezas, rotación, fusión).
- El **prompt de Kiro** sugerido y cómo usar el flujo de spec driven development para construir la etapa.
- Fragmentos de código explicados y el **resultado esperado** (qué debe verse en la ventana).
- Una actividad práctica y retos opcionales para estudiantes avanzados.

### `docs/guia_estudiante_sin_kiro.md` (sin Kiro)

Misma estructura de 8 lecciones, pero orientada a la escritura manual del código:

- En lugar de prompts, una sección **"Escribe el código"** con el código que el
  estudiante debe teclear, explicado por bloques y coherente con los módulos reales.
- Explica el flujo de trabajo **autónomo**: escribir, ejecutar, leer los errores y depurar.
- Indica la **rama de Git** de cada lección para comparar el avance con la solución.
- Mantiene objetivos, conceptos nuevos, resultado esperado, actividad práctica y los mismos retos avanzados.

Mapa lección → etapa del proyecto:

1. Qué es una matriz y el tablero 10×20.
2. Las piezas como matrices y sus rotaciones alternativas.
3. Abrir la ventana de Pygame y dibujar la matriz con números.
4. La pieza que cae: movimiento y rotación.
5. Colisiones y fusión con el tablero.
6. Líneas completas, puntuación y fin del juego.
7. Estilo neón: mejorar solo la presentación.

### `docs/guia_instructor.md`

Guía docente separada, pensada para quien imparte el curso. Incluye:

- **Planificación por sesiones** con duración estimada de cada una.
- Objetivos y **puntos clave a reforzar** por sesión.
- **Errores comunes** anticipados (confundir filas/columnas, índices fuera de rango, olvidar copiar la matriz al fusionar) y cómo resolverlos.
- **Soluciones esperadas** de las actividades prácticas de cada sesión.
- **Criterios de evaluación y rúbrica**, en la línea del curso Snake (participación, tareas y proyecto final).
- Recomendaciones para **usar Kiro en el aula** (crear specs, escribir prompts y revisar el código generado).

## Organización del repositorio en ramas

El repositorio separa el **punto de partida** de la **solución** para que el
estudiante tenga algo que construir:

- **`inicio`**: plantilla de partida. Mismo andamiaje que `main` (estructura,
  `docs/`, `README.md`, `requirements.txt`, `assets/`, `tools/`, `tests/`), pero
  los módulos de `tetris/` son un **esqueleto**: firmas y docstrings idénticos a
  los de `main`, con el cuerpo reemplazado por `raise NotImplementedError(...)` y
  comentarios `TODO` que citan la lección. Como excepción didáctica, la pieza
  `T` queda resuelta como ejemplo en `piezas.py` y `COLORES` solo trae la entrada
  del fondo (`0`). `main.py` captura `NotImplementedError` y muestra un mensaje
  amable indicando qué falta.
- **`leccion-1-...` a `leccion-8-...`**: la solución de cada etapa, para comparar.
- **`main`**: la solución completa y la vitrina del proyecto (etiquetada `v1.0`).

El estudiante crea su rama de trabajo desde `inicio`
(`git checkout -b tetris-nombre origin/inicio`) y la completa siguiendo las guías.
La coherencia entre `inicio` y `main` se mantiene con el steering
`.kiro/steering/sincronizacion-rama-inicio.md`.

## Progresión del tutorial (etapas)

1. **Ventana con números**: abrir la ventana de Pygame y dibujar el tablero (matriz) mostrando los números de cada casilla.
2. **Pieza que cae**: una pieza baja sola y se dibuja (números) dentro de la ventana.
3. **Movimiento y rotación**: mover izquierda/derecha, bajar, rotar cambiando de matriz.
4. **Colisiones y fusión**: la pieza se detiene y se une al tablero; aparece la siguiente.
5. **Líneas y puntuación**: eliminar filas completas y contar puntos; fin del juego.
6. **Estilo neón**: reutilizar la misma lógica y cambiar el dibujo de cada celda a colores neón brillantes sobre fondo oscuro para un acabado muy vistoso.
7. **Sonidos y animaciones**: añadir sonidos sencillos al girar y al eliminar filas, y animaciones breves al fusionar y al eliminar líneas, todo en la capa de presentación.

Cada etapa es jugable/observable en la ventana de Pygame, manteniendo el estilo motivador y progresivo del curso Snake.
