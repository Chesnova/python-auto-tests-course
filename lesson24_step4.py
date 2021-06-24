# cd environments
# selenium_env\Scripts\activate.bat
# python lesson24_step4.py
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(1)
button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")
assert "successful" in message.text

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()