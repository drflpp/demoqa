from pages.textbox_page import TextBoxPage
import time
def test_clear(browser):
    tb_page = TextBoxPage(browser)

    tb_page.visit()

    tb_page.full_name_area.send_keys('tttttt')

    time.sleep(2)

    tb_page.full_name_area.clear()
    assert tb_page.full_name_area.get_text() == ''
