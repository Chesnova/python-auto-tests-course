from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third")
    input3.send_keys("test@test.test")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()