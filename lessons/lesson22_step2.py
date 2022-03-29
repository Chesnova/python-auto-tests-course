from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")


select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"

sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
sub_button.click()

time.sleep(5)
browser.quit()