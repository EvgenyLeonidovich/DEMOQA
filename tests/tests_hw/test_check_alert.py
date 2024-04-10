import time
from pages.alerts import Alerts

def test_alert(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.timerResult.click()
    time.sleep(5)
    assert page_alerts.alert()
