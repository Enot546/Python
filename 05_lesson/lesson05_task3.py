from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    log = "button.radius"
    push_log = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    push_log.click()
    push_log.send_keys("12345")

    sleep(1)

    push_log.clear()

    sleep(1)

    push_log.send_keys("54321")

    sleep(1)

finally:
    if driver:
        driver.quit()
