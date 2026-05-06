from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class reg:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self._driver.get("https://www.saucedemo.com/")

    def register(self):
        self._driver.find_element(By.NAME, "user-name").send_keys(
            "standard_user")
        self._driver.find_element(By.NAME, "password").send_keys(
            "secret_sauce")
        self._driver.find_element(By.NAME, "login-button").click()
