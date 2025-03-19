from pages.base_page import BasePage
from components.components import WebElement

class WebtablesPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.table = WebElement(driver, 'ReactTable', 'class')
        self.no_rows_found_block = WebElement(driver, 'div.rt-noData')
        self.delete_btns = WebElement(driver, "span[title='Delete']")
        self.edit_btns = WebElement(driver, "span[title='Edit']")
        self.add_btn = WebElement(driver, '#addNewRecordButton')
        self.submit_btn = WebElement(driver, '#submit')

        self.forma = WebElement(driver, '#userForm')

        self.first_name = WebElement(driver, 'firstName', 'id')
        self.last_name = WebElement(driver, 'lastName', 'id')
        self.email_area = WebElement(driver, '#userEmail')
        self.age_area = WebElement(driver, 'age', 'id')
        self.salary_area = WebElement(driver, 'salary', 'id')
        self.department_area = WebElement(driver, 'department', 'id')

        self.rows = WebElement(driver, 'rt-tr-group', 'class')
        self.previous_btn = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.next_btn = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.rows_select = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.total_pages = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span')
        self.num_page = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')


