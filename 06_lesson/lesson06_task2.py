from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("http://uitestingplayground.com/textinput")

Button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
Button.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

wait.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))
content = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

element = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(element)

driver.quit()
