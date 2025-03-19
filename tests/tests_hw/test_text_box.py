from pages.textbox_page import TextBoxPage
import time



def test_text_box(browser):
    tb_page = TextBoxPage(browser)

    tb_page.visit()

    full_name = 'daria'
    current_address = 'petrograd'
    tb_page.full_name_area.send_keys(full_name)
    tb_page.current_address_area.send_keys(current_address)
    tb_page.btn_submit.click_force()



    assert tb_page.down_text.exist()
    assert tb_page.down_address.exist()
    assert full_name in tb_page.down_text.get_text()
    assert current_address in tb_page.down_address.get_text()