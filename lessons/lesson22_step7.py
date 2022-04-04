import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name) # добавляем к этому пути имя файла 
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

time.sleep(5)
browser.quit()