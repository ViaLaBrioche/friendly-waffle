from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ModalCard(BasePage):
    BTN_ADD_TO_CART = (By.XPATH, '//button[contains(., "Add to cart")]')
    BTN_PROCEED_TO_CHECKOUT = (By.XPATH, '//a[contains(., "Proceed to checkout")]')

    def add_to_cart(self):
        self.click(self.BTN_ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.BTN_PROCEED_TO_CHECKOUT)
