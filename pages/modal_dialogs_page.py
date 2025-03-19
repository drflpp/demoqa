from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_menu = WebElement(driver, '.btn')
        self.main_icon = WebElement(driver, '#app > header > a')
        self.small_mdl_btn = WebElement(driver, '#showSmallModal')
        self.large_mdl_btn = WebElement(driver, '#showLargeModal')
        self.modal_window = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.modal_close_btn = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal-header > button')
        self.close_large_mdl_btn = WebElement(driver, '#closeLargeModal')
        self.close_small_mdl_btn = WebElement(driver, '#closeSmallModal')