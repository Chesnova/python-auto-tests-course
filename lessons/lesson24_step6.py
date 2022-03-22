# cd environments
# selenium_env\Scripts\activate.bat
# python lesson24_step6.py
from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд


browser.get("http://suninjuly.github.io/cats.html")

browser.find_element_by_id("button")


    # закрываем браузер после всех манипуляций
browser.quit()