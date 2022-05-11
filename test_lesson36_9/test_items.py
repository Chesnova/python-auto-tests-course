import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")

    assert button, "There is no button"

# pytest -s -v --user_language=fr test_lesson36_9/test_items.py
# pytest -s -v --browser_name=firefox --user_language=fr test_lesson36_9/test_items.py