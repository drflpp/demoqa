from pages.base_page import BasePage
from components.components import WebElement

class AccordianPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.first_answer_text = WebElement(driver, '#section1Content > p')
        self.first_quastion_text = WebElement(driver, '#section1Heading')

        self.second_answer_one_text = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.second_answer_two_text = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.third_answer_text = WebElement(driver, '#section3Content > p')