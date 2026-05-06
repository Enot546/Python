import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Page.RegPage import reg
from Page.MainPage import proverka
from Page.CartPage import korzina
from Page.ResultPage import end


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()))
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()


def test_shop(driver):
    regpage = reg(driver)
    regpage.open()
    regpage.register()

    mainpage = proverka(driver)
    mainpage.tovar()

    cartpage = korzina(driver)
    cartpage.check()

    respage = end(driver)
    respage.result()
