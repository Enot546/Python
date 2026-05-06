import pytest
from Page.MainCalculater import calc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()


def test_calculater(driver):
    page = calc(driver)
    page.open()
    page.delay()
    page.input()
    page.wait_for_result()
    page.result()
