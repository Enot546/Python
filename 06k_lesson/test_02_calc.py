import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculator(driver: WebDriver):
    wait = WebDriverWait(driver, 90)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    time = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")))
    time.clear()
    time.send_keys("45")

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))).click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))).click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))).click()

    wait = WebDriverWait(driver, 50)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    result_element = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result_element == "15"
