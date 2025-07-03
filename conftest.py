from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page.saby_page import SabyPage
import pytest


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def page_saby(driver):
    driver.get('https://saby.ru/')
    yield SabyPage(driver)

