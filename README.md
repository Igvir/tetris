# Tetris con Matrices — Lección 8: Sonidos y animaciones (versión final)

Esta rama corresponde a la **Lección 8**, el pulido final del juego. Añadimos
**sonidos** (al rotar y al eliminar filas) y una **animación** de destello al
fusionar una pieza. El audio es **opcional**: si no hay archivos de sonido, el
juego funciona igual. La lógica de matrices sigue intacta.

Esta rama contiene el juego **completo**, equivalente a `main`.

## Qué aprenderás
- Reproducir sonidos con `pygame.mixer` de forma opcional y segura.
- Crear animaciones breves con un contador de fotogramas (sin bloquear el bucle).
- Confirmar que la lógica no depende de la presentación.

## Instalar y ejecutar

```bash
pip install -r requirements.txt
python main.py            # estilo neón
python main.py numeros    # estilo números
```

Controles: ← → mover, ↑ rotar, ↓ bajar, barra espaciadora caída instantánea,
R reiniciar, Esc salir.

Los sonidos van en `assets/sonidos/` (`giro.wav`, `linea.wav`). Si no existen,
el juego suena en silencio pero funciona igual.

## Probar la lógica

```bash
python -m pytest tests/
```

## Lecciones
- Anterior: `git checkout leccion-7-neon`
- Volver al juego completo: `git checkout main`

La guía completa está en [docs/guia_estudiante.md](docs/guia_estudiante.md) de la rama `main`.
