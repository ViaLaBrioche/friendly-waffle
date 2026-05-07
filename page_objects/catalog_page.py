from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CatalogPage(BasePage):
    CURRENCY_PRODUCT = (By.XPATH, '//span[@class="price"]')
    CURRENCY_SET = (By.XPATH, '//span[@class="expand-more _gray-darker"]')
    PAGE_URL = "/3-clothes"
    CATEGORIES = (By.XPATH, '//div[@class="block-categories"]')
    FILTERS_BRANDS = (By.CSS_SELECTOR, "#search_filters_brands")
    SUBCATEGORIES = (By.CSS_SELECTOR, "#subcategories")
    CARD_BLOCK = (By.XPATH, '//div[@class="block-category card card-block"]')
    SEARCH_FILTERS = (By.XPATH, '//div[@id="search_filters"]')

    def check_currency_symbol(self):
        self.driver.logger.info("Check currency symbol")
        currency_set = self.get_text(self.CURRENCY_SET)
        currency_product = self.get_text(self.CURRENCY_PRODUCT)
        return currency_product.strip()[0] == currency_set.split()[-1]

    def wait_until_loaded(self):
        self.wait_visible(self.CATEGORIES)

    def wait_until_currency_changed_to_usd(self, timeout=10):
        self.driver.logger.info("Wait until currency changed to USD")
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.CURRENCY_PRODUCT, "$"),
            message="Цена не обновилась на USD",
        )

    def check_required_elements_visible(self):
        self.driver.logger.info("Check required elements visible")
        self.wait_visible(self.CATEGORIES)
        self.wait_visible(self.FILTERS_BRANDS)
        self.wait_visible(self.SUBCATEGORIES)
        self.wait_visible(self.CARD_BLOCK)
        self.wait_visible(self.SEARCH_FILTERS)
