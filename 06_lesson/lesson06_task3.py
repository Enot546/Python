from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 30).until(EC.visibility_of_element_located
                                ((By.CSS_SELECTOR, "#landscape")))

find = driver.find_element(By.CSS_SELECTOR, "#award")
f = find.get_attribute("src")

print(f)

driver.quit
