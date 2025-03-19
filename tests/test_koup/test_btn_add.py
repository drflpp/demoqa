from pages.herokuapp_page import HeroKuAppPage
from pages.herokuapp_add_remove_page import HeroKuAppAddRemovePage
def test_btn_add(browser):
    hero_page = HeroKuAppPage(browser)
    hero_add_remove_page = HeroKuAppAddRemovePage(browser)
    hero_page.visit()

    assert hero_page.add_remove_elements_link.get_text() == 'Add/Remove Elements'

    hero_page.add_remove_elements_link.click()

    assert hero_add_remove_page.equal_url()

    assert hero_add_remove_page.add_elements_btn.get_text() == 'Add Element'
    assert hero_add_remove_page.add_elements_btn.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        hero_add_remove_page.add_elements_btn.click()

    assert hero_add_remove_page.delete_btn.check_count_elements(4)

    for el in hero_add_remove_page.delete_btn.find_elements():
        assert el.text == 'Delete'
    while hero_add_remove_page.delete_btn.exist():
        hero_add_remove_page.delete_btn.click()

    assert not hero_add_remove_page.delete_btn.exist()
    assert hero_add_remove_page.delete_btn.check_count_elements(0)