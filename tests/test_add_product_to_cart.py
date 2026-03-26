from page_objects.cart_page import CartPage
from page_objects.elements.modal_product import ModalCard
from page_objects.main_page import MainPage


def test_elements_is_visible_on_admin_login_page(driver, prestashop_base_url):
    main = MainPage(driver)
    cart = CartPage(driver)
    modal = ModalCard(driver)
    main.open(prestashop_base_url)
    main.wait_until_loaded()
    product_name = cart.get_product_name()
    cart.choose_product()
    modal.add_to_cart()
    modal.go_to_cart()
    cart.wait_until_loaded()
    product_name_cart = cart.get_product_name_in_cart()
    assert product_name.lower().replace("...", "") in product_name_cart.lower()
