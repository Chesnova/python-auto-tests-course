import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_cart(browser):
    browser.get(link)
    # time.sleep(30)
    try:
        button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    except:
        assert False, "Button add to cart is not found!"

# pytest -s -v --user_language=fr test_lesson36_9/test_items.py

