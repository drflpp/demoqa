from pages.modal_dialogs_page import ModalDialogsPage
from pages.demoqa import DemoQa
# def test_modal_elements(browser):
#     md_page = ModalDialogsPage(browser)
#
#     md_page.visit()
#     assert md_page.btns_menu.check_count_elements(5)

def test_navigation_modal(browser):
    md_page = ModalDialogsPage(browser)
    demo_qa_page = DemoQa(browser)
    md_page.visit()
    browser.refresh()
    md_page.main_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)

