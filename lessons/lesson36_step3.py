import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
# def test_guest_should_see_login_link(browser, number):
#     link = f"https://stepik.org/lesson/{number}/step/1"
#     browser.get(link)
#     area = browser.find_element(By.CLASS_NAME, "ember-text-area")
#     answer = math.log(int(time.time()))
#     area.send_keys(answer)
#     browser.find_element(By.CLASS_NAME, "submit-submission").click()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    area = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ember-text-area"))
    )
    area.send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    feedback = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    feedback_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text

    assert feedback_text == "Correct!"
    print(feedback_text)



# pytest -s -v lessons/lesson36_step3.py


