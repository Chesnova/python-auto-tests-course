# cd environments
# selenium_env\Scripts\activate.bat
# python lesson24_step6.py
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд


browser.get("http://suninjuly.github.io/cats.html")

browser.find_element(By.ID, "button")


    # закрываем браузер после всех манипуляций
browser.quit()