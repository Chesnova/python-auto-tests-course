from selenium import webdriver
import time
from selenium.webdriver.common.by import By

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    # Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    # Посчитать математическую функцию от x (код для этого приведён ниже).
    y = calc(x)

    form = browser.find_element(By.ID, "answer")
    # Ввести ответ в текстовое поле.
    form.send_keys(y)

    # Отметить checkbox "I'm the robot".
    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()
    # Выбрать radiobutton "Robots rule!".
    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

    # Нажать на кнопку Submit.
    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sub_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()