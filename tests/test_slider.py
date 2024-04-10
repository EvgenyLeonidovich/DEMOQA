from selenium.webdriver import Keys
from pages.slider import Slider

def test_slider(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider_cont.exist()
    assert slider.slider_value.exist()

    while not slider.slider_value.get_dom_attribute('value') == '50':
        slider.slider_cont.send_keys(Keys.ARROW_RIGHT)

    assert slider.slider_value.get_dom_attribute('value') == '50'
