from pages.demoqa import DemoQa
from components.components import WebElement
from pages.elements_page import ElementsPage

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.text_element.get_text()
    expected_text =  '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert demo_qa_page.text_element.equal_text(expected_text)

def test_check_text_centered(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()

    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()

    #demo_qa_page.text_element.get_text()
    expected_text = 'Please select an item from left to start practice.'

    assert demo_qa_page.center_text.get_text() == expected_text

    text_align = demo_qa_page.center_text.get_css_value('text-align')
    assert text_align == 'center'