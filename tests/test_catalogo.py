from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage


def test_catalogo(driver):

    login = LoginPage(driver)

    driver.get("https://www.saucedemo.com/")

    login.hacer_login(
        "standard_user",
        "secret_sauce"
    )

    assert driver.title == "Swag Labs"

    section_title = driver.find_element(
        By.CLASS_NAME, "title"
    ).text

    assert section_title == "Products"

    inventory_items = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    assert len(inventory_items) > 0

    menu_button = driver.find_element(
        By.ID, "react-burger-menu-btn"
    )

    assert menu_button.is_displayed()

    product_sort = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )

    assert product_sort.is_displayed()