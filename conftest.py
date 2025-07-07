import os
import pytest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page.saby_page import SabyPage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    if rep.when == "call" and rep.failed:
        driver = None
        for fixture_name in item.fixturenames:
            if fixture_name in ("driver", "driver_for_download"):
                driver = item.funcargs[fixture_name]
                break
        if driver is not None and isinstance(driver, webdriver.Remote):
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.nodeid.split("::")[-1]
            screenshot_name = f"{test_name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to: {screenshot_path}")


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
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
        "safebrowsing.enabled": False,
        "download.open_pdf_in_system_reader": False,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
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

