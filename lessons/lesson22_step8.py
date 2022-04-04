import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.NAME, "firstname").send_keys("Lava")
browser.find_element(By.NAME, "lastname").send_keys("Roma")
browser.find_element(By.NAME, "email").send_keys("test@test.test")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file_example.txt")
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

browser.find_element(By.CLASS_NAME, "btn").click()

time.sleep(5)
browser.quit()