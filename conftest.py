import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():

    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_argument("--lang=es")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    driver.implicitly_wait(10)

    yield driver

    driver.quit()