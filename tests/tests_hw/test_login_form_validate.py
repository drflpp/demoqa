from pages.auto_pract_form_page import AutoPractFormPage


def test_login_form_validate(browser):
    auto_form_page = AutoPractFormPage(browser)
    auto_form_page.visit()

    assert auto_form_page.first_name_area.get_dom_attribute('placeholder')
    assert auto_form_page.last_name_area.get_dom_attribute('placeholder')
    assert auto_form_page.email_area.get_dom_attribute('placeholder')
    assert auto_form_page.email_area.get_dom_attribute('pattern')

    auto_form_page.btn_submit.click_force()
    assert auto_form_page.forma.get_dom_attribute('class') == 'was-validated'
