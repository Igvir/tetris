# Requisitos - Tetris con Matrices

## Introducción

Este documento define los requisitos de un proyecto educativo: construir un juego de **Tetris** en Python utilizando **Kiro** y la metodología de **Spec Driven Development** (desarrollo guiado por especificaciones y prompts).

El proyecto es la evolución natural del curso anterior [snake_game](https://github.com/Igvir/snake_game). Mientras que el Snake enseñó los fundamentos de Python (variables, listas, tuplas, bucles, condicionales y una introducción a Pygame), este proyecto da el siguiente paso conceptual: **el manejo de matrices (listas de listas)**.

La idea pedagógica central es que **todo en Tetris es una matriz**:

- El tablero de juego es una matriz de 10 columnas × 20 filas.
- Cada pieza es una matriz pequeña, donde `0` representa una casilla vacía y un número (1 a 7) representa una casilla ocupada.
- La rotación de una pieza no calcula nada complejo: simplemente **cambia la matriz de la pieza por otra matriz predefinida** (sus rotaciones alternativas).
- Cuando una pieza toca la base del tablero u otra pieza, su matriz se **funde** (se copia) dentro de la matriz del tablero.

El curso avanza en versiones incrementales usando **siempre una ventana gráfica de Pygame**. Al principio, la ventana **dibuja los números** de las matrices (para que el estudiante vea directamente los datos: `0` en vacío y el número de la pieza en las casillas ocupadas). Más adelante se evoluciona la presentación a **colores neón** muy vistosos, reutilizando exactamente la misma lógica de matrices. Esto permite que el estudiante primero comprenda la estructura de datos y su lógica, y luego mejore únicamente la capa visual.

## Público objetivo y estilo

- Estudiantes de programación (nivel principiante-intermedio), en la línea del curso Snake para edades de 11-12 años en adelante.
- Todo el material, comentarios de código y textos del juego en **español**.
- Progresivo: cada requisito se construye sobre el anterior, mostrando avance visible en cada etapa.

## Requisitos

### Requisito 1: Representación del tablero como matriz

**Historia de usuario:** Como estudiante, quiero que el tablero del juego se represente como una matriz de números, para entender cómo una lista de listas modela una cuadrícula de juego.

#### Criterios de aceptación

1. CUANDO el juego inicia ENTONCES el sistema DEBERÁ crear una matriz de 20 filas por 10 columnas.
2. CUANDO se crea el tablero ENTONCES cada casilla vacía DEBERÁ contener el valor `0`.
3. CUANDO se solicita mostrar el tablero ENTONCES el sistema DEBERÁ imprimir la matriz mostrando los números de cada casilla.
4. CUANDO una casilla está ocupada ENTONCES DEBERÁ contener un número distinto de `0` que identifica la pieza que la ocupa.
5. EL sistema DEBERÁ exponer las dimensiones del tablero como constantes (ancho = 10, alto = 20) para facilitar su reutilización.

### Requisito 2: Representación de las piezas como matrices

**Historia de usuario:** Como estudiante, quiero que cada pieza (tetrominó) se defina como una matriz pequeña de números, para entender cómo una forma se representa con datos.

#### Criterios de aceptación

1. EL sistema DEBERÁ definir las 7 piezas clásicas de Tetris: I, O, T, S, Z, J, L.
2. CUANDO se define una pieza ENTONCES DEBERÁ representarse como una matriz donde `0` es casilla vacía y un número del 1 al 7 identifica la pieza.
3. CADA pieza DEBERÁ tener un número identificador único y constante (por ejemplo, I=1, O=2, T=3, S=4, Z=5, J=6, L=7).
4. CUANDO se solicita mostrar una pieza ENTONCES el sistema DEBERÁ imprimir su matriz con los números correspondientes.

### Requisito 3: Rotación mediante matrices alternativas

**Historia de usuario:** Como estudiante, quiero que al rotar una pieza simplemente se cambie su matriz por otra predefinida, para entender que la rotación puede resolverse con datos en lugar de cálculos complejos.

#### Criterios de aceptación

1. CADA pieza DEBERÁ tener definidas todas sus matrices de rotación (estados) posibles.
2. CUANDO el jugador rota una pieza ENTONCES el sistema DEBERÁ reemplazar la matriz actual por la siguiente matriz de rotación de esa pieza.
3. CUANDO se rota desde el último estado de rotación ENTONCES el sistema DEBERÁ volver al primer estado (rotación cíclica).
4. LA rotación NO DEBERÁ calcular la transformación matemática; DEBERÁ seleccionar una matriz ya definida en los datos de la pieza.
5. SI una rotación provocaría que la pieza salga del tablero o choque con otra pieza ENTONCES el sistema DEBERÁ rechazar la rotación y mantener el estado anterior.

### Requisito 4: Caída y movimiento de las piezas

**Historia de usuario:** Como jugador, quiero que las piezas caigan y poder moverlas, para jugar al Tetris.

#### Criterios de aceptación

1. CUANDO aparece una pieza nueva ENTONCES DEBERÁ posicionarse en la parte superior central del tablero.
2. CADA cierto intervalo de tiempo ENTONCES la pieza activa DEBERÁ descender una fila.
3. CUANDO el jugador presiona izquierda o derecha ENTONCES la pieza DEBERÁ moverse una columna en esa dirección si el movimiento es válido.
4. CUANDO el jugador presiona abajo ENTONCES la pieza DEBERÁ descender más rápido.
5. SI un movimiento llevaría la pieza fuera de los límites del tablero o sobre una casilla ocupada ENTONCES el sistema DEBERÁ rechazar el movimiento.

### Requisito 5: Detección de colisiones y fusión con el tablero

**Historia de usuario:** Como jugador, quiero que las piezas se detengan al tocar la base u otra pieza y se integren al tablero, para que se acumulen como en el Tetris clásico.

#### Criterios de aceptación

1. CUANDO la pieza activa no puede descender más porque tocaría la base del tablero ENTONCES el sistema DEBERÁ fusionar su matriz con la matriz del tablero.
2. CUANDO la pieza activa no puede descender más porque tocaría una casilla ocupada ENTONCES el sistema DEBERÁ fusionar su matriz con la matriz del tablero.
3. CUANDO se fusiona una pieza ENTONCES los números de la pieza DEBERÁN copiarse en las posiciones correspondientes de la matriz del tablero.
4. DESPUÉS de fusionar una pieza ENTONCES el sistema DEBERÁ generar una nueva pieza activa.
5. LA detección de colisión DEBERÁ recorrer las casillas ocupadas (valor distinto de `0`) de la matriz de la pieza y comparar con la matriz del tablero.

### Requisito 6: Eliminación de líneas completas

**Historia de usuario:** Como jugador, quiero que las filas completas desaparezcan, para que el juego progrese como el Tetris clásico.

#### Criterios de aceptación

1. CUANDO una fila del tablero tiene todas sus casillas ocupadas (ningún `0`) ENTONCES el sistema DEBERÁ eliminar esa fila.
2. CUANDO se elimina una fila ENTONCES las filas superiores DEBERÁN desplazarse hacia abajo.
3. CUANDO se elimina una fila ENTONCES DEBERÁ añadirse una nueva fila vacía (llena de `0`) en la parte superior.
4. CUANDO se eliminan una o más líneas ENTONCES el sistema DEBERÁ incrementar la puntuación.

### Requisito 7: Fin del juego

**Historia de usuario:** Como jugador, quiero que el juego termine cuando ya no hay espacio, para tener un objetivo y reto.

#### Criterios de aceptación

1. CUANDO una pieza nueva no puede colocarse en la posición inicial porque hay casillas ocupadas ENTONCES el sistema DEBERÁ terminar el juego.
2. CUANDO el juego termina ENTONCES el sistema DEBERÁ mostrar la puntuación final.
3. CUANDO el juego termina ENTONCES el sistema DEBERÁ ofrecer reiniciar o salir.

### Requisito 8: Versión numérica en ventana Pygame (Etapa 1)

**Historia de usuario:** Como estudiante, quiero una primera versión gráfica en Pygame que dibuje los números de las matrices, para comprender la estructura de datos viendo directamente los valores en pantalla.

#### Criterios de aceptación

1. LA primera versión jugable DEBERÁ ejecutarse en una ventana gráfica de Pygame (no en la terminal).
2. CUANDO se dibuja el tablero ENTONCES cada casilla DEBERÁ mostrar su número dibujado como texto dentro de la cuadrícula.
3. LA representación numérica DEBERÁ distinguir claramente casillas vacías (`0`) de casillas ocupadas (número de pieza).
4. CUANDO el estado del juego cambia ENTONCES la ventana DEBERÁ redibujarse mostrando la matriz actualizada con la pieza activa incluida.
5. LA ventana DEBERÁ dibujar la cuadrícula del tablero para que se distingan las 10×20 celdas.

### Requisito 9: Evolución a colores neón (Etapa 2)

**Historia de usuario:** Como jugador, quiero que la versión gráfica evolucione a un estilo de colores neón muy vistoso, para tener una experiencia visual atractiva del Tetris.

#### Criterios de aceptación

1. CADA número de pieza (1 a 7) DEBERÁ asociarse a un color neón distinto y brillante.
2. CUANDO se dibuja el tablero ENTONCES cada casilla ocupada DEBERÁ pintarse con el color neón correspondiente a su número, y las vacías con un fondo oscuro.
3. EL estilo neón DEBERÁ usar un fondo oscuro y colores saturados con efecto de brillo/contorno para resaltar las piezas.
4. LA lógica de matrices DEBERÁ reutilizarse sin cambios entre la versión numérica y la versión con colores neón; solo cambia la capa de dibujo.
5. LA versión gráfica DEBERÁ mostrar la puntuación en pantalla con el mismo estilo visual.

### Requisito 9b: Sonidos y animaciones

**Historia de usuario:** Como jugador, quiero escuchar sonidos sencillos al girar una pieza y al eliminar una fila, y ver una pequeña animación al fusionar una pieza, para que el juego sea más vistoso y con mejor respuesta.

#### Criterios de aceptación

1. CUANDO el jugador rota una pieza con éxito ENTONCES el sistema DEBERÁ reproducir un sonido corto de giro.
2. CUANDO se elimina una o más filas completas ENTONCES el sistema DEBERÁ reproducir un sonido de línea eliminada.
3. CUANDO una pieza se fusiona con el tablero ENTONCES el sistema DEBERÁ mostrar una animación breve (por ejemplo, un destello o parpadeo neón en las casillas recién fusionadas).
4. CUANDO se eliminan filas ENTONCES el sistema DEBERÍA mostrar una animación breve de las filas antes de que desaparezcan (por ejemplo, un parpadeo).
5. LOS sonidos DEBERÁN ser archivos sencillos y ligeros, cargados a través de Pygame (`pygame.mixer`).
6. SI un archivo de sonido no está disponible o el mezclador de audio no se puede inicializar ENTONCES el juego DEBERÁ continuar sin fallar (el audio es opcional y degradable).
7. LAS animaciones NO DEBERÁN bloquear el bucle de juego de forma perceptible; DEBERÁN durar pocos fotogramas.
8. LA lógica de matrices DEBERÁ permanecer sin cambios; los sonidos y animaciones DEBERÁN vivir en la capa de presentación (Pygame).

### Requisito 10: Estructura del proyecto y aprendizaje

**Historia de usuario:** Como estudiante, quiero que el proyecto esté organizado y documentado como un tutorial, para poder seguirlo paso a paso con Kiro.

#### Criterios de aceptación

1. EL proyecto DEBERÁ incluir un `README.md` en español que explique los objetivos de aprendizaje y cómo ejecutar el juego.
2. EL proyecto DEBERÁ incluir un `requirements.txt` con las dependencias (Pygame).
3. EL código DEBERÁ estar comentado en español, explicando el uso de las matrices.
4. LA lógica del juego (matrices, colisiones, rotaciones) DEBERÁ estar separada de la capa de presentación (Pygame) para poder reutilizarse.
5. EL tutorial DEBERÁ presentar el desarrollo en etapas incrementales, siguiendo el estilo progresivo del curso Snake.
6. EL `README.md` DEBERÁ incluir las instrucciones de entrega de la asignación mediante Git: clonar el repositorio, crear una rama con el nombre del estudiante y abrir un Pull Request al terminar.
7. LAS instrucciones de entrega DEBERÁN incluir los comandos concretos de Git (clonar, crear y cambiar de rama, confirmar, subir la rama y abrir el PR).
8. LAS instrucciones DEBERÁN explicar que el Pull Request es la evidencia de que el estudiante completó la asignación.

### Requisito 11: Guía del curso para el estudiante

**Historia de usuario:** Como estudiante, quiero una guía del curso que me lleve paso a paso por la construcción del Tetris usando Kiro y spec driven development, para aprender el manejo de matrices mientras construyo el juego.

#### Criterios de aceptación

1. EL proyecto DEBERÁ incluir una guía del estudiante en español, organizada en lecciones o sesiones progresivas.
2. LA guía DEBERÁ explicar el concepto de matrices (listas de listas) y cómo se aplican al tablero y a las piezas antes de escribir código.
3. CADA lección DEBERÁ incluir los objetivos de aprendizaje, los conceptos nuevos y una actividad práctica.
4. LA guía DEBERÁ mostrar cómo usar Kiro y los prompts (spec driven development) para construir cada etapa del juego.
5. LA guía DEBERÁ seguir la progresión de etapas del proyecto: ventana con números primero y colores neón al final.
6. LA guía DEBERÁ incluir fragmentos de código explicados y los resultados esperados en cada etapa.
7. LA guía DEBERÁ incluir ideas de mejoras o retos para estudiantes avanzados, en el estilo del curso Snake.

### Requisito 12: Guía del instructor

**Historia de usuario:** Como instructor, quiero una guía docente que me indique cómo enseñar el curso, cuánto tiempo dedicar a cada tema y cómo evaluar, para poder impartir el tutorial con confianza.

#### Criterios de aceptación

1. EL proyecto DEBERÁ incluir una guía del instructor en español, separada de la guía del estudiante.
2. LA guía del instructor DEBERÁ proponer una planificación por sesiones con la duración estimada de cada una.
3. LA guía del instructor DEBERÁ indicar los objetivos de aprendizaje y los puntos clave a reforzar en cada sesión.
4. LA guía del instructor DEBERÁ anticipar errores comunes de los estudiantes (por ejemplo, confundir filas y columnas, índices fuera de rango) y cómo resolverlos.
5. LA guía del instructor DEBERÁ incluir criterios de evaluación y una rúbrica, en la línea del curso Snake (participación, tareas y proyecto final).
6. LA guía del instructor DEBERÁ incluir soluciones o respuestas esperadas de las actividades prácticas de cada sesión.
7. LA guía del instructor DEBERÁ recomendar cómo usar Kiro en el aula (uso de specs, prompts y revisión del código generado).
