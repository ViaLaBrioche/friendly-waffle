import allure

from page_objects.product_card_page import ProductCardPage


@allure.title("Check product card page required elements")
@allure.description("Check that required elements are visible on product card page")
def test_elements_is_visible_on_product_card_page(driver, prestashop_base_url):
    product_card_page = ProductCardPage(driver)

    with allure.step("Open product card page"):
        product_card_page.open(prestashop_base_url)

    with allure.step("Check required elements visible on product card page"):
        product_card_page.check_required_elements_visible()
