from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    page_accordion = Accordion(browser)
    page_accordion.visit()

    assert page_accordion.section_1.visible()

    page_accordion.section.click()
    time.sleep(2)

    assert not page_accordion.section_1.visible()

def test_visible_accordion_default(browser):
    page_accordion_1 = Accordion(browser)
    page_accordion_1.visit()

    assert page_accordion_1.section_2.visible()
    assert page_accordion_1.section_3.visible()
    assert page_accordion_1.section_4.visible()

    assert not page_accordion_1.section_2.visible()
    assert not page_accordion_1.section_3.visible()
    assert not page_accordion_1.section_4.visible()
