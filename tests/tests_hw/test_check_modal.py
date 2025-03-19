from pages.modal_dialogs_page import ModalDialogsPage
from pages.alerts_page import AlertsPage
import pytest, time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_check_modal(browser):
    md_page = ModalDialogsPage(browser)
    md_page.visit()
    try:

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME,'h1'))
        )
    except TimeoutException:
        pytest.skip('Could not download the page')

    assert md_page.large_mdl_btn.exist()
    assert md_page.small_mdl_btn.exist()

    md_page.large_mdl_btn.click()
    assert md_page.modal_window.exist()
    md_page.close_large_mdl_btn.click()
    assert not md_page.modal_window.exist()

    md_page.small_mdl_btn.click()
    assert md_page.modal_window.exist()
    md_page.close_small_mdl_btn.click()
    assert not md_page.modal_window.exist()

def test_check_alert_timer_btn(browser):
    al_page = AlertsPage(browser)
    al_page.visit()
    al_page.alert_5_btn.click()
    time.sleep(8)
    assert al_page.alert()