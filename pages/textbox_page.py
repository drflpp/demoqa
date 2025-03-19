from pages.base_page import BasePage
from components.components import WebElement

class TextBoxPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)


        self.full_name_area = WebElement(driver, '#userName')
        self.current_address_area = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.down_text = WebElement(driver, '#name')
        self.down_address = WebElement(driver,locator="//p[@id='currentAddress' and contains(@class, 'mb-1')]", locator_type='xpath')
