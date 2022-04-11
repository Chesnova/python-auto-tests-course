from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    y = calc(x)

    form = browser.find_element(By.CLASS_NAME, "form-control")
    form.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()