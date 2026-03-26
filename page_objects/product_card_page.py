from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductCardPage(BasePage):
    PAGE_URL = "/2-9-brown-bear-printed-sweater.html#/1-size-s"
    PICTURE = (By.XPATH, '//div[@class="product-cover"]/picture')
    CONTENT = (By.CSS_SELECTOR, "#content")
    BUTTON_ADD_TO_CART = (By.XPATH, '//button[contains(., "Add to cart")]')
    COMMENTS_LIST = (By.XPATH, '//div[@id="product-comments-list-header"]')
    TAB_CONTENT = (By.XPATH, '//div[@id="tab-content"]')

    def check_required_elements_visible(self):
        self.wait_visible(self.PICTURE)
        self.wait_visible(self.CONTENT)
        self.wait_visible(self.BUTTON_ADD_TO_CART)
        self.wait_visible(self.COMMENTS_LIST)
        self.wait_visible(self.TAB_CONTENT)
