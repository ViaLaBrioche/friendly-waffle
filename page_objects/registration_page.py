# page_objects/registration_page.py

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class Registration(BasePage):
    PAGE_URL = "/registration"
    PAGE_CONTENT = (By.XPATH, '//div[@id="center-column"]')
    BTN_SAVE = (By.XPATH, '//button[contains(., "Create account")]')
    WRAPPER = (By.CSS_SELECTOR, "#wrapper")
    FIRST_NAME = (By.XPATH, '//input[@id="field-firstname"]')
    LAST_NAME = (By.CSS_SELECTOR, "#field-lastname")
    PASSWORD = (By.XPATH, '//input[@id="field-password"]')
    EMAIL = (By.CSS_SELECTOR, "#field-email")
    BIRTH_DATE = (By.CSS_SELECTOR, "#field-birthday")
    GENDER_MR = (By.CSS_SELECTOR, "label[for='field-id_gender_1']")
    GENDER_MRS = (By.CSS_SELECTOR, "label[for='field-id_gender_2']")

    I_AGREE_CHECKBOX = (By.XPATH, '//input[@id="field-psgdpr"]')
    NEWSLETTER_CHECKBOX = (By.XPATH, '//input[@id="field-newsletter"]')
    CUSTOMER_PRIVACY_CHECKBOX = (
        By.XPATH,
        '//input[@id="field-customer_privacy"]',
    )

    def check_required_elements_visible(self):
        self.driver.logger.info("Check registration page required elements visible")
        self.wait_visible(self.PAGE_CONTENT)
        self.wait_visible(self.BTN_SAVE)
        self.wait_visible(self.WRAPPER)
        self.wait_visible(self.FIRST_NAME)
        self.wait_visible(self.PASSWORD)

    def wait_until_loaded(self):
        self.wait_visible(self.FIRST_NAME)

    def select_social_title(self, gender):
        self.driver.logger.info("Select social title")
        genders = {"mr": self.GENDER_MR, "mrs": self.GENDER_MRS}
        self.click(genders[gender])

    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME, last_name)

    def enter_email(self, email):
        self.send_keys(self.EMAIL, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def enter_birthdate(self, birthdate):
        self.send_keys(self.BIRTH_DATE, birthdate)

    def set_i_agree(self):
        self.driver.logger.info("Set I agree checkbox")
        self.click(self.I_AGREE_CHECKBOX)

    def set_newsletter(self):
        self.driver.logger.info("Set newsletter checkbox")
        self.click(self.NEWSLETTER_CHECKBOX)

    def set_customer_privacy(self):
        self.driver.logger.info("Set customer privacy checkbox")
        self.click(self.CUSTOMER_PRIVACY_CHECKBOX)

    def save_information(self):
        self.driver.logger.info("Save registration form")
        self.click(self.BTN_SAVE)
