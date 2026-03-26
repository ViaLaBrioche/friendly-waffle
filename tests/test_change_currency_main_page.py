from page_objects.elements.header import Header
from page_objects.main_page import MainPage


def test_change_currency_main_page(driver, prestashop_base_url):
    main = MainPage(driver)
    header = Header(driver)
    main.open(prestashop_base_url)
    main.wait_until_loaded()
    main.check_currency_symbol()
    header.change_currency_to_usd()
    main.wait_until_currency_changed_to_usd()
    main.check_currency_symbol()
