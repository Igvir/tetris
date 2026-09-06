# 🎮 Tetris con Matrices en Python

Proyecto educativo para aprender el manejo de **matrices (listas de listas)** en Python construyendo un **Tetris** con **Kiro** y **spec driven development**.

Es la evolución del curso anterior [snake_game](https://github.com/Igvir/snake_game): mientras Snake enseñó los fundamentos (variables, listas, tuplas, bucles y una introducción a Pygame), aquí damos el siguiente paso conceptual: **todo en Tetris es una matriz**.

## 🧠 La gran idea: todo es una matriz

- El **tablero** es una matriz de 10 columnas × 20 filas.
- Cada **pieza** es una matriz donde `0` es una casilla vacía y un número del 1 al 7 la identifica.
- **Rotar** no calcula nada: solo cambia la matriz de la pieza por otra predefinida.
- Al tocar la base u otra pieza, la matriz de la pieza se **fusiona** (se copia) en la matriz del tablero.

El curso avanza por etapas: primero la ventana de Pygame dibuja los **números** de las matrices, y al final evoluciona a un vistoso estilo de **colores neón**, con sonidos y animaciones.

## 🎯 Objetivos de aprendizaje

- Entender y manipular matrices (listas de listas).
- Recorrer matrices con bucles anidados (`fila`, luego `columna`).
- Separar la **lógica** del juego de la **presentación** (Pygame).
- Detectar colisiones, fusionar piezas y eliminar líneas.
- Usar Kiro y specs para construir un proyecto paso a paso.

## 📋 Requisitos

- Python 3.8 o superior
- Pygame 2.5.2

## 🚀 Instalación

```bash
# 1. (Recomendado) crear un entorno virtual
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt
```

## ▶️ Cómo jugar

```bash
python main.py            # estilo neón (por defecto)
python main.py numeros    # estilo números (Etapa 1 del tutorial)
```

### Controles

| Tecla        | Acción                       |
|--------------|------------------------------|
| ← →          | Mover la pieza a los lados   |
| ↑            | Rotar la pieza               |
| ↓            | Bajar más rápido             |
| Barra espacio| Caída instantánea            |
| R            | Reiniciar (al terminar)      |
| Esc          | Salir                        |

## 📁 Estructura del proyecto

```
tetris/
├── tetris/
│   ├── piezas.py     # Matrices de cada pieza, rotaciones y colores neón
│   ├── tablero.py    # Matriz del tablero: crear, validar, fusionar, líneas
│   ├── juego.py      # Lógica del juego: pieza activa, movimiento, puntuación
│   ├── grafico.py    # Presentación en Pygame (números y neón) + animaciones
│   └── audio.py      # Sonidos opcionales con pygame.mixer
├── assets/sonidos/   # Sonidos (giro.wav, linea.wav) — opcionales
├── docs/
│   ├── guia_estudiante.md   # Curso paso a paso para el estudiante
│   └── guia_instructor.md   # Guía docente: planificación, evaluación, soluciones
├── tests/            # Pruebas de la lógica de matrices
├── main.py           # Punto de entrada
├── requirements.txt
└── README.md
```

## 📚 Guías del curso

- **[Guía del estudiante](docs/guia_estudiante.md)** — lecciones progresivas con prompts de Kiro.
- **[Guía del instructor](docs/guia_instructor.md)** — planificación, errores comunes, soluciones y rúbrica.

## 🧪 Pruebas

```bash
python -m pytest tests/
```

## 📝 Entrega de la asignación

La entrega se realiza mediante **Git**. Debes crear una rama con tu nombre y abrir un **Pull Request**: ese PR es la evidencia de que completaste la asignación.

```bash
# 1. Clona el repositorio
git clone <url-del-repositorio>
cd tetris

# 2. Crea una rama con tu nombre
git checkout -b tetris-nombre-apellido

# 3. Trabaja en tu solución y guarda los cambios
git add .
git commit -m "Completa la asignacion de Tetris"

# 4. Sube tu rama
git push -u origin tetris-nombre-apellido

# 5. Abre un Pull Request hacia la rama principal desde la interfaz de GitHub
```

> El **Pull Request** es la prueba de que terminaste la asignación. Asegúrate de que tu rama lleve tu nombre y de describir brevemente lo que hiciste en la descripción del PR.

## 💡 Ideas de mejora

- Niveles de velocidad que aumentan con las líneas.
- Mostrar la próxima pieza.
- Guardar el récord en un archivo.
- Más efectos neón (resplandor, degradados, destello al hacer un Tetris).

## 📄 Licencia

Proyecto educativo de uso libre.
