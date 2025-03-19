from pages.webtables_page import WebtablesPage
import time
from selenium.webdriver.common.keys import Keys
def test_table_disabled(browser):
    wb_page = WebtablesPage(browser)
    wb_page.visit()

    wb_page.rows_select.scroll_to_element()
    wb_page.rows_select.click()
    wb_page.rows_select.clear()
    wb_page.rows_select.send_keys('5 rows')
    wb_page.rows_select.send_keys(Keys.ENTER)

    time.sleep(2)

    first_name = 'daria'
    last_name = 'wow'
    email = 'name@example.com'
    age = '24'
    salary = '90000'
    department = 'dept'

    for i in range(2):
        wb_page.add_btn.click()

        wb_page.first_name.send_keys(first_name)
        wb_page.last_name.send_keys(last_name)
        wb_page.email_area.send_keys(email)
        #time.sleep(2)
        wb_page.age_area.send_keys(age)
        wb_page.salary_area.send_keys(salary)
        wb_page.department_area.send_keys(department)

        wb_page.submit_btn.click()
        #time.sleep(2)

    assert wb_page.previous_btn.get_dom_attribute('disabled')
    assert wb_page.next_btn.get_dom_attribute('disabled')

    for i in range(3):
        wb_page.add_btn.click()

        wb_page.first_name.send_keys(first_name)
        wb_page.last_name.send_keys(last_name)
        wb_page.email_area.send_keys(email)
        #time.sleep(2)
        wb_page.age_area.send_keys(age)
        wb_page.salary_area.send_keys(salary)
        wb_page.department_area.send_keys(department)

        wb_page.submit_btn.click()
        time.sleep(2)

    assert wb_page.total_pages.get_text() == '2'
    wb_page.next_btn.click()
    assert wb_page.num_page.get_dom_attribute('value') == '2'
    wb_page.previous_btn.click()
    assert wb_page.num_page.get_dom_attribute('value') == "1"
