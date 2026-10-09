
from pages.LoginPage import LoginPage


def iniciar_sesion(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.hacer_login(
        "standard_user",
        "secret_sauce"
    )
