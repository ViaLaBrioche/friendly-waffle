import allure

from page_objects.catalog_page import CatalogPage
from page_objects.elements.header import Header


@allure.title("Change currency on catalog page")
@allure.description("Check that currency can be changed to USD on catalog page")
def test_change_currency_catalog_page(driver, prestashop_base_url):
    header = Header(driver)
    catalog = CatalogPage(driver)

    with allure.step("Open catalog page"):
        catalog.open(prestashop_base_url)

    with allure.step("Wait until catalog page loaded"):
        catalog.wait_until_loaded()

    with allure.step("Check currency symbol before change"):
        assert catalog.check_currency_symbol(), (
            "Currency symbol before change is incorrect"
        )

    with allure.step("Change currency to USD"):
        header.change_currency_to_usd()

    with allure.step("Wait until currency changed to USD"):
        catalog.wait_until_currency_changed_to_usd()

    with allure.step("Check currency symbol after change to USD"):
        assert catalog.check_currency_symbol(), (
            "Currency symbol after change to USD is incorrect"
        )
