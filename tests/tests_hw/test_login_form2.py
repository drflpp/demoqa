from pages.auto_pract_form_page import AutoPractFormPage
from selenium.webdriver.common.keys import Keys
import time
def test_login_form(browser):
    auto_form_page = AutoPractFormPage(browser)
    auto_form_page.visit()

    auto_form_page.state_btn.scroll_to_element()
    auto_form_page.state_btn.find_element()
    auto_form_page.state_btn.click()
    auto_form_page.inp_state.send_keys(Keys.PAGE_DOWN)
    auto_form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)

    auto_form_page.city_btn.find_element()
    auto_form_page.city_btn.click()
    auto_form_page.inp_city.send_keys(Keys.PAGE_DOWN)
    auto_form_page.inp_city.send_keys(Keys.ENTER)
    time.sleep(2)
