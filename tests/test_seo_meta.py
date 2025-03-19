from pages.demoqa import DemoQa
from pages.accordian_page import AccordianPage
from pages.alerts_page import AlertsPage
from pages.browser_tab import BrowserTabPage
import time
import pytest
#from pages.elements_page import ElementsPage


@pytest.mark.parametrize("pages", [AccordianPage, AlertsPage, DemoQa, BrowserTabPage])
def test_check_title(browser, pages):
    #demo_qa_page = DemoQa(browser)
    #el_page = ElementsPage(browser)
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'

