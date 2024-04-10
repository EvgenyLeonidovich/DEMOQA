from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQA

def test_modal_elements(browser):
    page_modal_dialogs = ModalDialogs(browser)

    page_modal_dialogs.visit()

    assert page_modal_dialogs.btns_modal_dialogs.check_count_elements(5)

def test_navigation_modal(browser):
    page_modal = ModalDialogs(browser)
    demo = DemoQA(browser)

    page_modal.visit()
    page_modal.refresh()
    page_modal.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
