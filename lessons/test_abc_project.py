import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class TestAbc(unittest.TestCase):
    def test_abc1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"

        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third")
        input3.send_keys("test@test.test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "test_abc1      failed")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_abc2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"

        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first")
        input1.send_keys("Ivan")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third")
        input3.send_keys("test@test.test")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations!", "test_abc2 failed")

        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    unittest.main()

# python lessons/test_abc_project.py
# pytest lessons/test_abc_project.py