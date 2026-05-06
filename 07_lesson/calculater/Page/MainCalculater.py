from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class calc:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-"
            "java/slow-calculator.html")

    def delay(self):
        time = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        time.clear()
        time.send_keys("45")

    def input(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait_for_result(self):
        WebDriverWait(self._driver, 47).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))

    def result(self):
        result = self._driver.find_element(
            By.CSS_SELECTOR, ".screen").text
        assert result == "15"
