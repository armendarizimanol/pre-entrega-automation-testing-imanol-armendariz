# Pre-entrega QA Automation

Este proyecto corresponde a la pre-entrega del curso de QA Automation.

La idea es realizar pruebas automatizadas sobre la página SauceDemo utilizando Python, Selenium y Pytest.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager
- pytest-html

## Estructura del proyecto

```text
pre_entrega_QA_automation/
│
├── pages/
│   └── LoginPage.py
│
├── tests/
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
│
├── utils/
│   └── helpers.py
│
├── reports/
│   └── reporte.html
│
├── conftest.py
├── pytest.ini
├── README.md
└── .gitignore
```

- **pages:** contiene la clase `LoginPage`, donde se encuentran los elementos y acciones relacionados con el inicio de sesión.
- **tests:** contiene las pruebas automatizadas de login, catálogo y carrito.
- **utils:** contiene funciones auxiliares que se utilizan en las pruebas, como el inicio de sesión.
- **reports:** guarda el reporte HTML generado por Pytest.
- **conftest.py:** configura el navegador que utilizan las pruebas.
- **pytest.ini:** contiene la configuración de Pytest para generar el reporte.

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

## Cómo instalar las dependencias

Con Python instalado, ejecutar el siguiente comando en la terminal:

```bash
pip install pytest selenium webdriver-manager pytest-html
```

## Cómo ejecutar las pruebas

Desde la carpeta principal del proyecto, ejecutar:

```bash
python -m pytest
```

## Reporte

Al ejecutar las pruebas, se genera automáticamente un reporte HTML en:

```text
reports/reporte.html
```

El reporte permite consultar los resultados de las pruebas ejecutadas.

## Page Object Model

Para el inicio de sesión se utilizó una clase llamada `LoginPage`, donde se encuentran los localizadores y las acciones relacionadas con el login.

Además, se utiliza `utils/helpers.py` para reutilizar la función de inicio de sesión en los distintos tests.

## Resultado

En la última ejecución, las cinco pruebas finalizaron correctamente:

```text
5 passed in 16.41s
```