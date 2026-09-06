# Plan de implementación - Tetris con Matrices

Las tareas siguen la progresión del tutorial: siempre se trabaja sobre una ventana de Pygame. Primero la ventana dibuja los números de las matrices y al final la presentación evoluciona a colores neón. Cada tarea es incremental y termina en algo observable, en el estilo del curso Snake.

- [x] 1. Preparar el proyecto y las bases del curso
  - Crear la estructura de carpetas (`tetris/`, `tests/`) y el paquete con `__init__.py`.
  - Crear `requirements.txt` (Pygame) y un `README.md` inicial en español con objetivos de aprendizaje y cómo ejecutar.
  - _Requisitos: 10.1, 10.2, 10.5_

- [x] 2. Definir el tablero como matriz
  - [x] 2.1 Crear el tablero vacío
    - Implementar `crear_tablero(ancho=10, alto=20)` que devuelva una matriz de `0`.
    - Exponer constantes `ANCHO = 10` y `ALTO = 20`.
    - _Requisitos: 1.1, 1.2, 1.5_
  - [x] 2.2 Utilidad para depurar el tablero
    - Implementar `mostrar_tablero(tablero)` que imprima la matriz en terminal distinguiendo `0` de casillas ocupadas (solo para depuración).
    - _Requisitos: 1.3, 1.4_

- [x] 3. Definir las piezas como matrices con sus rotaciones
  - [x] 3.1 Crear las matrices de las 7 piezas
    - Definir `PIEZAS` (nombre -> lista de matrices de rotación) y `NUMERO_PIEZA` (I=1 ... L=7).
    - Rellenar cada pieza con su número identificador y `0` en las casillas vacías.
    - _Requisitos: 2.1, 2.2, 2.3_
  - [x] 3.2 Mostrar una pieza y elegir una al azar
    - Implementar utilidades para imprimir la matriz de una pieza y `pieza_aleatoria()`.
    - _Requisitos: 2.4_

- [x] 4. Implementar la lógica de rotación por matrices alternativas
  - Añadir a `Juego` el índice de `rotacion` y `matriz_pieza_actual()`.
  - Implementar `rotar()` que avance cíclicamente al siguiente estado y solo lo aplique si es válido.
  - _Requisitos: 3.1, 3.2, 3.3, 3.4, 3.5_

- [x] 5. Implementar colisiones (validación de posición)
  - Implementar `es_valida(tablero, matriz, fila, columna)` recorriendo solo las casillas ocupadas de la pieza.
  - Rechazar posiciones fuera de límites y sobre casillas ocupadas.
  - _Requisitos: 4.5, 5.5_

- [x] 6. Implementar caída y movimiento de la pieza activa
  - [x] 6.1 Estado de la pieza activa y aparición
    - Crear la clase `Juego` con `tablero`, `pieza`, `rotacion`, `fila`, `columna`, `puntuacion`, `terminado`.
    - Implementar `nueva_pieza()` que posicione la pieza en la parte superior central.
    - _Requisitos: 4.1_
  - [x] 6.2 Movimiento horizontal y descenso
    - Implementar `mover(dx)` y `bajar()` respetando `es_valida`.
    - Permitir descenso acelerado con la tecla abajo.
    - _Requisitos: 4.2, 4.3, 4.4, 4.5_
  - [x] 6.3 Dibujar la pieza sobre el tablero
    - Implementar `tablero_con_pieza()` que devuelva una copia del tablero con la pieza activa incluida (para mostrar).
    - _Requisitos: 8.2_

- [x] 7. Implementar fusión de la pieza con el tablero
  - Implementar `fusionar(tablero, matriz, fila, columna)` copiando los números distintos de `0`.
  - En `bajar()`, cuando no se pueda descender, fusionar y luego generar una nueva pieza.
  - _Requisitos: 5.1, 5.2, 5.3, 5.4_

- [x] 8. Implementar eliminación de líneas y puntuación
  - Implementar `lineas_completas(tablero)` y `eliminar_lineas(tablero)` (desplazar hacia abajo y añadir filas vacías arriba).
  - Incrementar la puntuación según las líneas eliminadas.
  - _Requisitos: 6.1, 6.2, 6.3, 6.4_

- [x] 9. Implementar fin del juego
  - Detectar cuando una pieza nueva no cabe en la posición inicial y marcar `terminado`.
  - Mostrar la puntuación final y ofrecer reiniciar o salir.
  - _Requisitos: 7.1, 7.2, 7.3_

- [x] 10. Ventana de Pygame con estilo números (Etapa 1)
  - [x] 10.1 Abrir la ventana y dibujar la cuadrícula
    - Crear `grafico.py` que inicialice Pygame, cree la ventana y el reloj, y dibuje la cuadrícula 10×20.
    - Crear `main.py` como punto de entrada y manejar el cierre de ventana limpiamente.
    - _Requisitos: 8.1, 8.5_
  - [x] 10.2 Dibujar la matriz como números
    - Recorrer `tablero_con_pieza()` y dibujar el número de cada casilla como texto; `0` como celda vacía.
    - Redibujar la ventana en cada cambio de estado y mostrar la puntuación.
    - _Requisitos: 8.2, 8.3, 8.4_
  - [x] 10.3 Conectar el teclado y el bucle de juego
    - Leer teclado para mover, rotar y bajar; aplicar el descenso automático por tiempo.
    - Reutilizar la clase `Juego` sin cambios.
    - _Requisitos: 4.2, 4.3, 4.4_

- [x] 11. Evolucionar la presentación a colores neón (Etapa 2)
  - [x] 11.1 Colores neón por número de pieza
    - Definir `COLORES` (número -> RGB neón) para las 7 piezas y el fondo oscuro.
    - _Requisitos: 9.1_
  - [x] 11.2 Dibujar las celdas con estilo neón
    - Reemplazar el dibujo de números por rectángulos con color neón, fondo oscuro para `0` y contorno claro para simular el brillo.
    - Mantener la puntuación en pantalla con el mismo estilo visual.
    - Reutilizar la clase `Juego` y toda la lógica sin cambios.
    - _Requisitos: 9.2, 9.3, 9.4, 9.5_

- [x] 11b. Añadir sonidos y animaciones (pulido)
  - [x] 11b.1 Sonidos con pygame.mixer
    - Crear `audio.py` con `iniciar_audio()`, `cargar_sonidos()` y `reproducir(nombre)`, con degradación segura si no hay audio.
    - Añadir archivos de sonido sencillos en `assets/sonidos/` (giro y línea eliminada).
    - Reproducir el sonido de giro al rotar con éxito y el de línea al eliminar filas.
    - _Requisitos: 9b.1, 9b.2, 9b.5, 9b.6, 9b.8_
  - [x] 11b.2 Animación al fusionar
    - Mostrar un destello/parpadeo neón breve en las casillas recién fusionadas, controlado por un contador de fotogramas.
    - _Requisitos: 9b.3, 9b.7, 9b.8_
  - [x] 11b.3 Animación al eliminar filas
    - Mostrar un parpadeo breve de las filas completas antes de eliminarlas.
    - _Requisitos: 9b.4, 9b.7, 9b.8_

- [x] 12. Pruebas de la lógica de matrices
  - Escribir pruebas para crear tablero, fusionar, `es_valida`, `eliminar_lineas` y rotación cíclica.
  - _Requisitos: 1.1, 1.2, 3.3, 5.5, 6.1_

- [x] 13. Completar el README del proyecto
  - [x] 13.1 Contenido general del README
    - Completar `README.md`: descripción, objetivos de aprendizaje, requisitos, instalación, cómo ejecutar el juego e índice que enlaza a las guías de `docs/`.
    - Verificar que la lógica esté separada de la presentación (Requisito 10.4) y que el código esté comentado en español.
    - _Requisitos: 10.1, 10.3, 10.4, 10.5_
  - [x] 13.2 Instrucciones de entrega con Git
    - Añadir la sección "Entrega de la asignación": clonar el repositorio, crear una rama con el nombre del estudiante, confirmar, subir la rama y abrir un Pull Request.
    - Incluir los comandos concretos de Git y aclarar que el Pull Request es la evidencia de que completó la asignación.
    - _Requisitos: 10.6, 10.7, 10.8_

- [x] 14. Escribir la guía del estudiante (`docs/guia_estudiante.md`)
  - [x] 14.1 Introducción a matrices y estructura de las lecciones
    - Explicar qué es una matriz (lista de listas) y cómo modela el tablero 10×20 y las piezas.
    - Definir el formato de cada lección: objetivos, conceptos nuevos y actividad práctica.
    - _Requisitos: 11.1, 11.2, 11.3_
  - [x] 14.2 Lecciones por etapa con prompts de Kiro
    - Escribir una lección por etapa (matriz, piezas/rotación, ventana con números, caída/movimiento, colisiones/fusión, líneas/puntuación, neón, sonidos y animaciones).
    - Incluir en cada lección el prompt sugerido de Kiro y el flujo de spec driven development.
    - Incluir fragmentos de código explicados y el resultado esperado en la ventana.
    - _Requisitos: 11.4, 11.5, 11.6_
  - [x] 14.3 Retos para estudiantes avanzados
    - Añadir ideas de mejora (niveles de velocidad, pieza siguiente, guardado de récord, efectos neón extra).
    - _Requisitos: 11.7_

- [x] 14b. Escribir la guía del estudiante sin Kiro (`docs/guia_estudiante_sin_kiro.md`)
  - Crear una segunda guía con las mismas 8 lecciones, sin prompts ni agente, guiando a escribir el código a mano.
  - Explicar el flujo autónomo (escribir, ejecutar, leer errores, depurar) e indicar la rama de Git de cada lección.
  - Incluir objetivos, conceptos, resultado esperado, actividad práctica y los retos avanzados; enlazar con la guía con Kiro.
  - Enlazar ambas guías entre sí y actualizar README, spec y guía del instructor para documentar las dos rutas.
  - _Requisitos: 11b.1, 11b.2, 11b.3, 11b.4, 11b.5, 11b.6, 11b.7, 12.8_

- [x] 15. Escribir la guía del instructor (`docs/guia_instructor.md`)
  - [x] 15.1 Planificación por sesiones y objetivos
    - Proponer la planificación por sesiones con duración estimada, objetivos y puntos clave a reforzar.
    - _Requisitos: 12.1, 12.2, 12.3_
  - [x] 15.2 Errores comunes y soluciones de las actividades
    - Documentar errores frecuentes (filas vs columnas, índices fuera de rango, copiar la matriz al fusionar) y su solución.
    - Incluir las soluciones esperadas de las actividades prácticas de cada sesión.
    - _Requisitos: 12.4, 12.6_
  - [x] 15.3 Evaluación y uso de Kiro en el aula
    - Definir criterios de evaluación y rúbrica (participación, tareas, proyecto final).
    - Añadir recomendaciones para usar Kiro en clase (specs, prompts y revisión del código generado).
    - _Requisitos: 12.5, 12.7_
```
