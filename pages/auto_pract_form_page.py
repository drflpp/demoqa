from pages.base_page import BasePage
from components.components import WebElement


class AutoPractFormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)


        self.first_name_area = WebElement(driver, '#firstName')
        self.last_name_area = WebElement(driver, '#lastName')
        self.email_area = WebElement(driver, '#userEmail')
        self.btn_submit = WebElement(driver, '#submit')
        self.forma = WebElement(driver, '#userForm')
        self.state_btn = WebElement(driver, 'state', 'id')
        self.inp_state = WebElement(driver, '#react-select-3-input')
        #self.state_ncr = WebElement(driver,  "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[2]/div/div", 'xpath')
        self.city_btn = WebElement(driver, 'city', 'id')
        self.inp_city = WebElement(driver, '#react-select-4-input')
        #self.city_delhi = WebElement(driver, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]", 'xpath')