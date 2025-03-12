from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class WebElement:
    def __init__(self, driver, locator = ''):
        self.driver = driver
        self.locator = locator


    def click(self):
        return self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def equal_text(self, expected_text):
        if self.get_text() == expected_text:
            return True
        else:
            return False

    def get_css_value(self, property_name):
        return self.find_element().value_of_css_property(property_name)

    def visible(self):
        return self.find_element().is_displayed()