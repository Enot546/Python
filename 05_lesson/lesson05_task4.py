from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "username").send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CLASS_NAME, "radius").click()

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located
                         ((By.CSS_SELECTOR, "div[class='flash success']")))
finally:
    if driver:
        driver.quit()
