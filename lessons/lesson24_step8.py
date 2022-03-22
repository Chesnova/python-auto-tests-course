# cd environments
# selenium_env\Scripts\activate.bat
# python lesson24_step8.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    text = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Считать значение для переменной x.
    # Посчитать математическую функцию от x (код для этого приведён ниже).
    
    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    print(x_element)
    x = x_element.text
    print(x)
    y = calc(x)
    
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_css_selector("input#answer.form-control")
    input1.send_keys(y)
    # Нажать на кнопку Submit.  
    # Отправляем заполненную форму
    button1 = browser.find_element_by_css_selector("button#solve")
    button1.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()