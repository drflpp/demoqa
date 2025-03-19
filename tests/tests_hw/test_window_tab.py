from pages.links_page import LinksPage


def test_window_tab(browser):
    link_page = LinksPage(browser)
    link_page.visit()

    assert link_page.home_link.get_text() == 'Home'
    assert link_page.home_link.get_dom_attribute('href') == 'https://demoqa.com'

    link_page.home_link.click()

    assert len(browser.window_handles) == 2