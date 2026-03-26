from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminLoginPage(BasePage):
    PAGE_URL = ""
    LOGIN_CONTENT = (By.XPATH, '//div[@id="login-content-card"]')
    LOGIN_HEADER = (By.CSS_SELECTOR, "#login-header")
    BTN_LOGIN = (By.XPATH, '//button[contains(., "Log in")]')
    FORM_GROUP = (By.XPATH, '//div[@class="form-group"]')
    LOGIN_FOOTER = (By.XPATH, '//div[@id="login-footer"]')
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#passwd")
    BTN_SUBMIT = (By.CSS_SELECTOR, "#submit_login")
    BTN_PROFILE = (By.XPATH, '//li[@id="employee_infos"]')
    BTN_SIGN_OUT = (By.XPATH, '//a[@id="header_logout"]')

    def check_required_elements_visible(self):
        self.wait_visible(self.LOGIN_CONTENT)
        self.wait_visible(self.LOGIN_HEADER)
        self.wait_visible(self.BTN_LOGIN)
        self.wait_visible(self.FORM_GROUP)
        self.wait_visible(self.LOGIN_FOOTER)

    def wait_until_loaded_login_page(self):
        self.wait_visible(self.LOGIN_CONTENT)

    def enter_email(self, email):
        self.send_keys(self.EMAIL, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def click_log_in(self):
        self.click(self.BTN_SUBMIT)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_log_in()

    def is_logged_in(self):
        return self.wait_visible(self.BTN_PROFILE)

    def open_profile(self):
        self.click(self.BTN_PROFILE)

    def sign_out(self):
        self.click(self.BTN_SIGN_OUT)
