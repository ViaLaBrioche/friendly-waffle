from page_objects.product_card_page import ProductCardPage


def test_elements_is_visible_on_product_card_page(driver, prestashop_base_url):
    product_card_page = ProductCardPage(driver)
    product_card_page.open(prestashop_base_url)
    product_card_page.check_required_elements_visible()
