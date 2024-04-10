from pages.base_page import BasePage
from components.components import WebElement
class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.window = WebElement(driver, 'body > div.fade.modal.show')
        self.add_button = WebElement(driver, '#addNewRecordButton')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.submit_button = WebElement(driver, '#submit')
        self.pencil_button = WebElement(driver, '#edit-record-4 > svg')
        self.basket_button = WebElement(driver, '#delete-record-4 > svg')
        self.name = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.line = WebElement(driver, 'div.rt-tbody > div:nth-child(4)')
        self.sort_FName = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(1)')
        self.sort_LName = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(2)')
        self.sort_Age = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(3)')
        self.sort_Email = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(4)')
        self.sort_Salary = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(5)')
        self.sort_Dep = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(6)')
        self.sort_Action = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(7)')