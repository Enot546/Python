from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class proverka:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 10)

    def tovar(self):

        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

        self._driver.find_element(By.ID, "shopping_cart_container").click()
