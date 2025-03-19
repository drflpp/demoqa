from pages.webtables_page import WebtablesPage
import time
def test_sort(browser):
    wt_page = WebtablesPage(browser)

    wt_page.visit()

    for header in wt_page.column_headers.find_elements():
        header.click()
        time.sleep(2)
        assert '-sort' in header.get_dom_attribute('class')