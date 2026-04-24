import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_form(setup_driver: WebDriver):
    driver = setup_driver
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    wait = WebDriverWait(driver, 10)
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code_field.get_attribute("class")

    fields_to_check_green = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]
    for field_name in fields_to_check_green:
        field = wait.until(
            EC.presence_of_element_located((By.ID, field_name)))
    assert "alert-success" in field.get_attribute("class")
