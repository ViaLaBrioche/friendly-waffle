import allure

from page_objects.catalog_page import CatalogPage


@allure.title("Check catalog page required elements")
@allure.description("Check that required elements are visible on catalog page")
def test_elements_is_visible_on_catalog_page(driver, prestashop_base_url):
    catalog = CatalogPage(driver)

    with allure.step("Open catalog page"):
        catalog.open(prestashop_base_url)

    with allure.step("Check required elements visible on catalog page"):
        catalog.check_required_elements_visible()
