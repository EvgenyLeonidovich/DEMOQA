import time
from pages.page_webtables import Webtables

def test_webtables(browser):
    page = Webtables(browser)
    page.visit()
    class_etalon = 'rt-th rt-resizable-header -cursor-pointer'

    page.sort_FName.click()
    assert not page.sort_FName.get_dom_attribute('class') == f'{class_etalon}'
    page.sort_LName.click()
    assert not page.sort_LName.get_dom_attribute('class') == f'{class_etalon}'
    page.sort_Age.click()
    assert not page.sort_Age.get_dom_attribute('class') == f'{class_etalon}'
    page.sort_Email.click()
    assert not page.sort_Email.get_dom_attribute('class') == f'{class_etalon}'
    page.sort_Salary.click()
    assert not page.sort_Salary.get_dom_attribute('class') == f'{class_etalon}'
    page.sort_Dep.click()
    assert not page.sort_Dep.get_dom_attribute('class') == f'{class_etalon}'
    page.sort_Action.click()
    assert not page.sort_Action.get_dom_attribute('class') == f'{class_etalon}'
