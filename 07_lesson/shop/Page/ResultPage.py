from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class end:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 5)

    def result(self):

        self._driver.find_element(By.NAME, "firstName").send_keys("Артур")
        self._driver.find_element(By.NAME, "lastName").send_keys("Пирожков")
        self._driver.find_element(By.NAME, "postalCode").send_keys("606060")

        self._driver.find_element(By.ID, "continue").click()

        result_element = self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
        assert result_element == "Total: $58.29"
