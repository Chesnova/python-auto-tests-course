link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

# pytest -s -v --browser_name=firefox tests/test_parser.py

# pytest -s -v --browser_name=firefox --user_language=en tests/test_parser.py