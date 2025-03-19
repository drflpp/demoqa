from pages.alerts_page import AlertsPage
import time
def test_alerts(browser):
    al_page = AlertsPage(browser)

    al_page.visit()
    assert not al_page.alert()
    al_page.alert_btn.click()
    time.sleep(2)
    assert al_page.alert()
    al_page.alert().accept()

def test_alert_text(browser):
    al_page = AlertsPage(browser)

    al_page.visit()

    al_page.alert_btn.click()
    time.sleep(2)
    assert al_page.alert().text == 'You clicked a button'
    al_page.alert().accept()
    assert not al_page.alert()

def test_confirm(browser):
    al_page = AlertsPage(browser)

    al_page.visit()

    al_page.confirm_btn.click()
    time.sleep(2)
    al_page.alert().dismiss()
    assert al_page.confirm_result.get_text() == 'You selected Cancel'
    time.sleep(2)
    browser.refresh()
def test_prompt(browser):
    al_page = AlertsPage(browser)
    name = 'daria'
    al_page.visit()
    al_page.prompt_btn.click()
    time.sleep(2)
    al_page.alert().send_keys(name)
    al_page.alert().accept()
    assert al_page.prompt_result.get_text() == f'You entered {name}'