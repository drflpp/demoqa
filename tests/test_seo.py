from pages.demoqa import DemoQa
#from pages.elements_page import ElementsPage


def test_check_title(browser):
    demo_qa_page = DemoQa(browser)
    #el_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'