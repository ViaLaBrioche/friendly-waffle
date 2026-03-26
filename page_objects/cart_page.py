from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import random


class CartPage(BasePage):
    random_product_id = random.randint(1, 8)
    PRODUCT = (By.XPATH, f'//article[@data-id-product="{random_product_id}"]')
    PRODUCT_NAME = (By.XPATH, './/h3[@class="h3 product-title"]/a')
    BTN_ADD_TO_CART = (By.XPATH, '//button[contains(., "Add to cart")]')
    SOPPING_CART = (By.XPATH, '//h1[normalize-space()="Shopping Cart"]')
    PRODUCT_NAME_CART = (By.XPATH, './/div[@class="product-line-info"]/a')

    def get_product_name(self):
        product = self.wait_visible(self.PRODUCT)
        name = product.find_element(*self.PRODUCT_NAME).text
        return name

    def choose_product(self):
        self.click(self.PRODUCT)

    def wait_until_loaded(self):
        self.wait_visible(self.SOPPING_CART)

    def get_product_name_in_cart(self):
        return self.get_text(self.PRODUCT_NAME_CART)
