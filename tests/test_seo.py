import time

import pytest
from pages.demoqa import DemoQA
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab

def test_seo(browser):
    demo = DemoQA(browser)

    demo.visit()
    assert browser.title == 'DEMOQA'

@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQA, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page =pages(browser)
    page.visit()
    time.sleep(2)

    assert page.get_title() == 'DEMOQA'
