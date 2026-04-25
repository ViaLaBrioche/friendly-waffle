import allure
from page_objects.cart_page import CartPage
from page_objects.elements.modal_product import ModalCard
from page_objects.main_page import MainPage


@allure.title("Add product to cart")
@allure.description("Check add product to cart")
def test_add_product_to_cart(driver, prestashop_base_url):
    main = MainPage(driver)
    cart = CartPage(driver)
    modal = ModalCard(driver)

    with allure.step("Open main page"):
        main.open(prestashop_base_url)
        main.wait_until_loaded()

    with allure.step("Get selected product name"):
        product_name = cart.get_product_name()

    with allure.step("Choose product"):
        cart.choose_product()

    with allure.step("Add product to cart"):
        modal.add_to_cart()

    with allure.step("Go to cart"):
        modal.go_to_cart()

    with allure.step("Wait until cart page loaded"):
        cart.wait_until_loaded()

    with allure.step("Get product name from cart"):
        product_name_cart = cart.get_product_name_from_cart()

    with allure.step("Check product name in cart"):
        assert product_name.lower().replace("...", "") in product_name_cart.lower()
