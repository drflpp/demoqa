from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement
class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)
        self.icon = WebElement(driver, locator = '#app > header > a')
        self.btn_elements = WebElement(driver, locator='#app > div >div> div.home-body > div >div:nth-child(1)')
        self.text_element = WebElement(driver, locator='#app > footer > span')

        self.center_text = WebElement(driver, locator='#app > div > div > div > div.col-12.mt-4.col-md-6')