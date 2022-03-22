from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type=text]")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# python lesson16_step7.py