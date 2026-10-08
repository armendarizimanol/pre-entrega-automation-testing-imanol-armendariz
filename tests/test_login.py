from pages.LoginPage import LoginPage


def test_login(driver):

    login = LoginPage(driver)

    driver.get("https://www.saucedemo.com/")

    login.hacer_login(
        "standard_user",
        "secret_sauce"
    )

    assert "/inventory.html" in driver.current_url