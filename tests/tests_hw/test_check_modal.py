import time
from pages.modal_dialogs import ModalDialogs

def test_check_modal(browser):
    page = ModalDialogs(browser)
    page.visit()

    page.small_button.click()
    assert page.window_small.exist()
    page.close_small.click()
    assert not page.window_small.exist()

    page.large_button.click()
    assert page.window_large.exist()
    page.close_large.click()
    assert not page.window_large.exist()
