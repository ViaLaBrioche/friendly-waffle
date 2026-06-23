from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):
    LOGO = (By.XPATH, '//img[@class="logo img-fluid"]')
    SAMPLE = (By.XPATH, '//h2[normalize-space()="Sample 1"]')
    PAGE_URL = ""
    CURRENCY_SET = (By.XPATH, '//span[@class="expand-more _gray-darker"]')
    CURRENCY_PRODUCT = (By.XPATH, '//span[@class="price"]')
    HEADER = (By.XPATH, '//*[@id="header"]')
    BANNER = (By.XPATH, '//div[@class="carousel-item active"]')
    FOOTER_CONTAINER = (By.XPATH, '//footer[@id="footer"]')

    def wait_until_loaded(self):
        self.wait_visible(self.LOGO)

    def check_currency_symbol(self):
        self.driver.logger.info("Check currency symbol")
        currency_set = self.get_text(self.CURRENCY_SET)
        currency_product = self.get_text(self.CURRENCY_PRODUCT)
        return currency_product.strip()[0] == currency_set.split()[-1]

    def wait_until_currency_changed_to_usd(self, timeout=10):
        self.driver.logger.info("Wait until currency changed to USD")
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.CURRENCY_PRODUCT, "$"),
            message="Цена не обновилась на USD",
        )

    def check_required_elements_visible(self):
        self.driver.logger.info("Check required elements visible")
        self.wait_visible(self.LOGO)
        self.wait_visible(self.HEADER)
        self.wait_visible(self.BANNER)
        self.wait_visible(self.FOOTER_CONTAINER)
        self.wait_visible(self.SAMPLE)
