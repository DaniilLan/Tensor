import os

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
def driver_for_download():
    chrome_options = Options()
    download_path = os.path.join(os.getcwd(), "test_downloads")
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": False

    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.execute_cdp_cmd("Page.setDownloadBehavior", {
        "behavior": "allow",
        "downloadPath": download_path
    })
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def page_saby(driver):
    driver.get('https://saby.ru/')
    yield SabyPage(driver)


@pytest.fixture()
def download_page(driver_for_download):
    driver_for_download.get('https://saby.ru/')
    yield SabyPage(driver_for_download)

