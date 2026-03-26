from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Registration(BasePage):
    PAGE_URL = "/registration"
    PAGE_CONTENT = (By.XPATH, '//div[@class="page-content card card-block"]')
    BTN_SAVE = (By.XPATH, '//button[contains(., "Save")]')
    WRAPPER = (By.CSS_SELECTOR, "#wrapper")
    FIRST_NAME = (By.XPATH, '//input[@id="field-firstname"]')
    LAST_NAME = (By.CSS_SELECTOR, "#field-firstname")
    PASSWORD = (By.XPATH, '//input[@id="field-password"]')
    EMAIL = (By.CSS_SELECTOR, "#field-email")
    BIRTH_DATE = (By.CSS_SELECTOR, "#field-birthday")
    GENDER_MR = (By.CSS_SELECTOR, "label[for='field-id_gender-1']")
    GENDER_MRS = (By.CSS_SELECTOR, "label[for='field-id_gender-2']")
    RECEIVE_OFFERS_CHECKBOX = (By.XPATH, '//input[@name="optin"]')
    I_AGREE_CHECKBOX = (By.XPATH, '//input[@name="psgdpr"]/parent::label')
    NEWSLETTER_CHECKBOX = (By.XPATH, '//input[@name="newsletter"]/parent::label')
    CUSTOMER_PRIVACY_CHECKBOX = (
        By.XPATH,
        '//input[@name="customer_privacy"]/parent::label',
    )

    def check_required_elements_visible(self):
        self.wait_visible(self.PAGE_CONTENT)
        self.wait_visible(self.BTN_SAVE)
        self.wait_visible(self.WRAPPER)
        self.wait_visible(self.FIRST_NAME)
        self.wait_visible(self.PASSWORD)

    def wait_until_loaded(self):
        self.wait_visible(self.FIRST_NAME)

    def select_social_title(self, gender):
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
        self.click(self.I_AGREE_CHECKBOX)

    def set_customer_privacy(self):
        self.click(self.CUSTOMER_PRIVACY_CHECKBOX)

    def set_newsletter(self):
        self.click(self.NEWSLETTER_CHECKBOX)

    def save_information(self):
        self.click(self.BTN_SAVE)
