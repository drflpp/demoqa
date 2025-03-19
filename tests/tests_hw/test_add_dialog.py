from pages.webtables_page import WebtablesPage
import time
def test_add_dialog(browser):
    wb_page = WebtablesPage(browser)
    wb_page.visit()

    wb_page.add_btn.click()
    wb_page.submit_btn.click()
    assert wb_page.forma.exist(), 'forma not found'

    wb_page.first_name.send_keys('daria')
    wb_page.last_name.send_keys('fly')
    wb_page.email_area.send_keys('name@example.com')
    time.sleep(2)
    wb_page.age_area.send_keys('45')
    wb_page.salary_area.send_keys('300000')
    wb_page.department_area.send_keys('fbt')

    wb_page.submit_btn.click()
    time.sleep(2)

    assert not wb_page.forma.exist(), 'forma found'

    new_record_found = False
    target_row = None
    i = 0
    for row in wb_page.rows.find_elements():
        if 'daria' in row.text and 'fly' in row.text and 'name@example.com' in row.text:
            new_record_found = True
            target_row = row
            i +=1
            break
        i +=1
    assert new_record_found == True
    assert target_row != None

    e = 1
    for edit_btn in wb_page.edit_btns.find_elements():

        if e == i:
            edit_btn.click()
            assert wb_page.first_name.get_dom_attribute('value') == 'daria'
            assert wb_page.last_name.get_dom_attribute('value') == 'fly'

            update_name = 'sasha'
            wb_page.first_name.clear()
            wb_page.first_name.send_keys(update_name)
            wb_page.submit_btn.click()
            time.sleep(2)
            break
        e = e + 1


    e = 1
    for delete_btn in wb_page.delete_btns.find_elements():
        if e == i:
            delete_btn.click()
            assert not target_row in wb_page.rows.find_elements()
            break

        e += 1





