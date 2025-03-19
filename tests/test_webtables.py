from pages.webtables_page import WebtablesPage

def test_webtables(browser):
    wt_page = WebtablesPage(browser)

    wt_page.visit()
    assert not wt_page.no_rows_found_block.exist()

    while wt_page.delete_btns.exist():
        wt_page.delete_btns.click_force()
    assert wt_page.no_rows_found_block.exist()

