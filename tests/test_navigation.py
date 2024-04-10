from pages.demoqa import DemoQA
from pages.elements import Elements

def test_navigation(browser):
    demo = DemoQA(browser)
    elements = Elements(browser)

    demo.visit()
    demo.btn_elements.get_text()

    elements.refresh()
    browser.refresh()

    browser.back()
    browser.forward()
    assert elements.equal_url()