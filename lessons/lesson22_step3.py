from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects1.html"

    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap").text
    num2 = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap").text

    sum_num = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_num)

    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sub_button.click()

finally:
    time.sleep(5)
    browser.quit()