from pages.auto_pract_form_page import AutoPractFormPage


def test_login_form(browser):
    auto_form_page = AutoPractFormPage(browser)
    auto_form_page.visit()

    auto_form_page.state_btn.find_element()
    auto_form_page.state_btn.click_force()
    auto_form_page.state_ncr.click_force()

    auto_form_page.city_btn.find_element()
    auto_form_page.city_btn.click_force()
    auto_form_page.city_delhi.click_force()
