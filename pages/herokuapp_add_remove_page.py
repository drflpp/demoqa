from pages.base_page import BasePage
from components.components import WebElement
class HeroKuAppAddRemovePage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.add_elements_btn = WebElement(driver, '#content > div > button')
        self.delete_btn = WebElement(driver, 'added-manually', 'class')