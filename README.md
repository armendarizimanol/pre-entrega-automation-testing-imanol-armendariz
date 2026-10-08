# Pre-entrega QA Automation

Este proyecto corresponde a la pre-entrega del curso de QA Automation.

La idea es realizar pruebas automatizadas sobre la página SauceDemo utilizando Python, Selenium y Pytest.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager
- pytest-html

## Pruebas realizadas

### Login

Se prueba el ingreso a SauceDemo utilizando un usuario y contraseña válidos y se verifica que se ingrese correctamente al catálogo.

### Catálogo

Se verifica:

- Que la página tenga el título correcto.
- Que aparezca la sección "Products".
- Que haya productos disponibles.
- Que el botón del menú sea visible.
- Que el selector de ordenamiento sea visible.

### Carrito

Se prueba:

- Agregar un producto al carrito.
- Verificar que el botón cambie a "Remove".
- Verificar el contador del carrito.
- Ingresar al carrito.
- Verificar que el producto agregado aparezca correctamente.

## Cómo ejecutar las pruebas

Primero instalar las librerías necesarias:

```bash
pip install pytest selenium webdriver-manager pytest-html