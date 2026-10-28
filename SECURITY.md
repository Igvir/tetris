# Política de seguridad

Este es un proyecto **educativo**: un juego de Tetris local escrito en Python
con Pygame. No tiene componentes de red, servidor, autenticación ni base de
datos, por lo que su superficie de ataque es muy reducida.

## Versiones soportadas

| Versión | Soportada |
|---------|-----------|
| 1.x     | ✅         |

Python soportado: **3.11 o superior** (probado en 3.11, 3.12 y 3.13).

## Alcance frente a OWASP

El [OWASP Top 10](https://owasp.org/www-project-top-ten/) está orientado a
aplicaciones web. Al ser un juego de escritorio local, la mayoría de categorías
no aplican. Lo que sí cuidamos:

- **A06 — Componentes vulnerables y desactualizados**: dependencias fijadas por
  versión y auditadas con `pip-audit`.
- **A08 — Fallos de integridad del software y de los datos**: versiones
  pinneadas para builds reproducibles; CI ejecuta las pruebas y los análisis de
  seguridad en cada cambio.
- **Manejo seguro de archivos**: la carga de recursos (sonidos) valida que las
  rutas permanezcan dentro de `assets/sonidos/`, evitando *path traversal*.

## Buenas prácticas de ejecución

- Usa siempre un entorno virtual (`python -m venv venv`).
- Instala solo desde `requirements.txt` / `pyproject.toml`.
- Ejecuta las auditorías antes de publicar cambios:

  ```bash
  pip install pip-audit bandit
  pip-audit -r requirements.txt
  bandit -r tetris main.py tools
  ```

## Cómo reportar una vulnerabilidad

Si encuentras un problema de seguridad, abre un *issue* en el repositorio
describiendo el problema y los pasos para reproducirlo. Al tratarse de un
proyecto educativo sin datos sensibles, no se requiere divulgación privada,
pero agradecemos un reporte claro y reproducible.
