import time
from pages.text_box import TextBox
from components.components import WebElement


def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('tester')
    text_box.current_address.send_keys('Saint-Petersburg')
    text_box.submit.click_force()
    assert text_box.element.check_count_elements(2)
    assert text_box.element.get_text() == "Name:tester" and "Current Address :Saint-Petersburg"
