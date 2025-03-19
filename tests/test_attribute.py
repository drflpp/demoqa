from pages.textbox_page import TextBoxPage
import time

def test_placeholder(browser):
    tb_page = TextBoxPage(browser)

    tb_page.visit()
    assert tb_page.full_name_area.get_dom_attribute('placeholder') == 'Full Name'