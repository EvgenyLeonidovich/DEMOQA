from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_modal_dialogs = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a')
        self.small_button = WebElement(driver, '#showSmallModal')
        self.close_small = WebElement(driver, '#closeSmallModal')
        self.window_small = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.large_button = WebElement(driver, '#showLargeModal')
        self.close_large = WebElement(driver, '#closeLargeModal')
        self.window_large = WebElement(driver, 'body > div.fade.modal.show > div > div')
