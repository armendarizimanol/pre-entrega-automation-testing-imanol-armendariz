
from utils.helpers import iniciar_sesion


def test_login(driver):

    iniciar_sesion(driver)

    assert "/inventory.html" in driver.current_url
