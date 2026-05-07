import allure

from page_objects.elements.header import Header
from page_objects.main_page import MainPage


@allure.title("Change currency on main page")
@allure.description("Check that currency can be changed to USD on main page")
def test_change_currency_main_page(driver, prestashop_base_url):
    main = MainPage(driver)
    header = Header(driver)

    with allure.step("Open main page"):
        main.open(prestashop_base_url)

    with allure.step("Wait until main page loaded"):
        main.wait_until_loaded()

    with allure.step("Check currency symbol before change"):
        assert main.check_currency_symbol(), (
            "Currency symbol before change is incorrect"
        )

    with allure.step("Change currency to USD"):
        header.change_currency_to_usd()

    with allure.step("Wait until currency changed to USD"):
        main.wait_until_currency_changed_to_usd()

    with allure.step("Check currency symbol after change to USD"):
        assert main.check_currency_symbol(), (
            "Currency symbol after change to USD is incorrect"
        )
