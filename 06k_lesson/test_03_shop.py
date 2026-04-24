import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shop(driver: WebDriver):
    wait = WebDriverWait(driver, 90)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    wait.until(
        EC.element_to_be_clickable((By.NAME, "login-button"))).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "shopping_cart_container"))).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout"))).click()

    driver.find_element(By.NAME, "firstName").send_keys("Артур")
    driver.find_element(By.NAME, "lastName").send_keys("Пирожков")
    driver.find_element(By.NAME, "postalCode").send_keys("606060")

    wait.until(
        EC.element_to_be_clickable((By.ID, "continue"))).click()

    result_element = driver.find_element(
        By.CSS_SELECTOR, ".summary_total_label").text
    assert result_element == "Total: $58.29"
