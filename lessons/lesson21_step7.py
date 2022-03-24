from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    form = browser.find_element(By.ID, "answer")
    form.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sub_button.click()

finally:
    time.sleep(5)
    browser.quit()