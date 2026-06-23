from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import random


class CartPage(BasePage):
    random_product_id = random.randint(1, 4)
    PRODUCT = (By.XPATH, f'//article[@data-id-product="{random_product_id}"]')
    PRODUCT_NAME = (By.XPATH, './/a[contains(@class, "product-miniature__title")]')
    BTN_ADD_TO_CART = (By.XPATH, '//button[contains(., "Add to cart")]')
    SHOPPING_CART = (By.XPATH, '//h1[normalize-space()="Shopping Cart"]')
    PRODUCT_NAME_CART = (By.XPATH, './/div[@class="product-line__content-left"]/a')

    def get_product_name(self):
        self.driver.logger.info("Get selected product name")
        product = self.wait_visible(self.PRODUCT)
        name = product.find_element(*self.PRODUCT_NAME).text
        return name

    def choose_product(self):
        self.driver.logger.info("Choose product")
        self.click(self.PRODUCT)

    def wait_until_loaded(self):
        self.wait_visible(self.SHOPPING_CART)

    def get_product_name_from_cart(self):
        self.driver.logger.info("Get product name from cart")
        return self.get_text(self.PRODUCT_NAME_CART)
