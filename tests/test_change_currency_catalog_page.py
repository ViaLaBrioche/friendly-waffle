from page_objects.catalog_page import CatalogPage
from page_objects.elements.header import Header


def test_change_currency_catalog_page(driver, prestashop_base_url):
    header = Header(driver)
    catalog = CatalogPage(driver)
    catalog.open(prestashop_base_url)
    catalog.wait_until_loaded()
    catalog.check_currency_symbol()
    header.change_currency_to_usd()
    catalog.wait_until_currency_changed_to_usd()
    catalog.check_currency_symbol()
