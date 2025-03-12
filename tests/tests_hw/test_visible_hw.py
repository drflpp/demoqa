from pages.accordian_page import AccordianPage
import time

def test_visible_accordian(browser):
    acc_page = AccordianPage(browser)

    acc_page.visit()
    assert acc_page.first_answer_text.visible()

    acc_page.first_quastion_text.click()
    time.sleep(2)
    assert not acc_page.first_answer_text.visible()


def test_visible_accordian_default(browser):
    acc_page = AccordianPage(browser)

    acc_page.visit()
    assert not acc_page.second_answer_one_text.visible()
    assert not acc_page.second_answer_two_text.visible()
    assert not acc_page.third_answer_text.visible()