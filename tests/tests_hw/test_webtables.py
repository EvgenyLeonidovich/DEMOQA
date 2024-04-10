import time
from pages.page_webtables import Webtables

def test_webtables(browser):
    page = Webtables(browser)
    page.visit()

    page.add_button.click()
    page.submit_button.click()
    assert page.window.exist()
    time.sleep(3)
    page.first_name.send_keys('tester')
    page.last_name.send_keys('testerovich')
    page.email.send_keys('test@test.ru')
    page.age.send_keys('26')
    page.salary.send_keys('450')
    page.department.send_keys('IT')
    page.submit_button.click()
    assert not page.window.exist()
    assert page.line.get_text() == 'tester\ntesterovich\n26\ntest@test.ru\n450\nIT'
    page.pencil_button.click()
    assert page.window.exist()
    page.first_name.clear()
    page.first_name.send_keys('Evgeny')
    page.submit_button.click()
    assert page.name.get_text() == 'Evgeny'
    page.basket_button.click()
    assert page.line.get_text() != ''