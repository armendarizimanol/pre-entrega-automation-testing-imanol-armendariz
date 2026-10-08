from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import LoginPage


def test_agregar_producto(driver):

    login = LoginPage(driver)

    driver.get("https://www.saucedemo.com/")

    login.hacer_login(
        "standard_user",
        "secret_sauce"
    )

    inventory_items = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    first_product = inventory_items[0]

    add_button = first_product.find_element(
        By.TAG_NAME, "button"
    )

    add_button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".inventory_item button"),
            "Remove"
        )
    )

    updated_product = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )[0]

    updated_button = updated_product.find_element(
        By.TAG_NAME, "button"
    )

    assert updated_button.text == "Remove"


def test_contador_carrito(driver):

    login = LoginPage(driver)

    driver.get("https://www.saucedemo.com/")

    login.hacer_login(
        "standard_user",
        "secret_sauce"
    )

    inventory_items = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    first_product = inventory_items[0]

    add_button = first_product.find_element(
        By.TAG_NAME, "button"
    )

    add_button.click()

    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert cart_badge.text == "1"


def test_navegar_carrito_y_verificar_producto(driver):

    login = LoginPage(driver)

    driver.get("https://www.saucedemo.com/")

    login.hacer_login(
        "standard_user",
        "secret_sauce"
    )

    inventory_items = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    first_product = inventory_items[0]

    product_name = first_product.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    add_button = first_product.find_element(
        By.TAG_NAME, "button"
    )

    add_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    cart_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert cart_product.text == product_name