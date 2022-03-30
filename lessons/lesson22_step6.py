from selenium import webdriver
from selenium.webdriver.common.by import By
import time


import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    y = calc(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);")

    form = browser.find_element(By.CLASS_NAME, "form-control")
    form.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

    button.click()



finally:
    time.sleep(5)
    browser.quit()