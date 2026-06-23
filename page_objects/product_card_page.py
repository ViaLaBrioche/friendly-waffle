from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductCardPage(BasePage):
    PAGE_URL = "/2-9-brown-bear-printed-sweater.html#/1-size-s"
    PICTURE = (By.XPATH, '//div[@class="carousel-item active"]/picture')
    CONTENT = (By.CSS_SELECTOR, "#center-column")
    BUTTON_ADD_TO_CART = (By.XPATH, '//button[contains(., "Add to cart")]')
    COMMENTS_LIST = (By.XPATH, '//div[@id="product-comments-list-header"]')
    PRODUCT_RIGHT = (By.XPATH, '//div[@class="product__right"]')

    def check_required_elements_visible(self):
        self.driver.logger.info("Check product card required elements visible")
        self.wait_visible(self.PICTURE)
        self.wait_visible(self.CONTENT)
        self.wait_visible(self.BUTTON_ADD_TO_CART)
        self.wait_visible(self.COMMENTS_LIST)
        self.wait_visible(self.PRODUCT_RIGHT)
