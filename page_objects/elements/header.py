from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class Header(BasePage):
    CURRENCY_DROPDOWN = (By.XPATH, '//span[@class="expand-more _gray-darker"]')
    USD_OPTION = (By.XPATH, '//a[@title="US Dollar"]')

    def change_currency_to_usd(self):
        self.click(self.CURRENCY_DROPDOWN)
        self.click(self.USD_OPTION)
