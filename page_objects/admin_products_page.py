from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminProductsPage(BasePage):
    PAGE_URL = "/sell/catalog/products"
    LINK_ADD_NEW_PRODUCT = (By.XPATH, "//a[@id='page-header-desc-configuration-add']")
    STANDARD_PRODUCT = (By.CSS_SELECTOR, 'button[data-value="standard"]')
    BTN_ADD_NEW_PRODUCT = (By.XPATH, "//button[contains(., 'Add new product')]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#product_header_name_1")
    MODAL_SELECT_PRODUCT_IFRAME = (By.XPATH, "//iframe[@class='visible']")
    DESCRIPTION_IFRAME = (By.CSS_SELECTOR, "#product_description_description_1_ifr")
    DESCRIPTION_BODY = (By.CSS_SELECTOR, "body")
    BTN_SAVE = (By.CSS_SELECTOR, "#product_footer_save")
    PRODUCT_FOR_DELETE = (By.XPATH, "//tbody/tr[1]/td[1]")
    BTN_BULK_ACTIONS = (By.XPATH, "//button[contains(., 'Bulk actions')]")
    BTN_DELETE_SELECTION = (
        By.XPATH,
        "//button[@id='product_grid_bulk_action_bulk_delete_ajax']",
    )
    BTN_DELETE_SELECTION_CONFIRM = (
        By.XPATH,
        "//div[@class='modal-footer']//button[contains(., 'Delete selection')]",
    )
    PROGRESS_MESSAGE = (By.XPATH, "//div[@class='progress-message']")

    def wait_until_loaded(self):
        self.wait_visible(self.LINK_ADD_NEW_PRODUCT)

    def add_new_product_main_page(self):
        self.driver.logger.info("Open add new product page")
        self.click(self.LINK_ADD_NEW_PRODUCT)

    def wait_until_product_creation_page_loaded(self):
        self.wait_visible(self.PRODUCT_NAME, timeout=30)

    def select_standard_product(self):
        iframe = self.wait_visible(self.MODAL_SELECT_PRODUCT_IFRAME, timeout=20)
        self.driver.switch_to.frame(iframe)
        standard_product = self.wait_clickable(self.STANDARD_PRODUCT, timeout=20)
        self.driver.execute_script("arguments[0].click();", standard_product)
        add_button = self.wait_clickable(self.BTN_ADD_NEW_PRODUCT, timeout=20)
        self.driver.execute_script("arguments[0].click();", add_button)
        self.driver.switch_to.default_content()
        self.wait_until_product_creation_page_loaded()

    def enter_product_name(self, product_name):
        self.send_keys(self.PRODUCT_NAME, product_name)

    def enter_product_description(self, description):
        self.driver.logger.info("Select standard product type")
        iframe = self.wait_visible(self.DESCRIPTION_IFRAME)
        self.driver.switch_to.frame(iframe)
        self.send_keys(self.DESCRIPTION_BODY, description)
        self.driver.switch_to.default_content()

    def save_product(self):
        self.driver.logger.info("Save product")
        self.click(self.BTN_SAVE)

    def choose_product(self):
        self.click(self.PRODUCT_FOR_DELETE)

    def open_actions(self):
        self.click(self.BTN_BULK_ACTIONS)

    def delete_product(self):
        self.driver.logger.info("Delete product")
        self.click(self.BTN_DELETE_SELECTION)

    def confirm_delete_product(self):
        self.driver.logger.info("Confirm delete product")
        self.click(self.BTN_DELETE_SELECTION_CONFIRM)

    def wait_deleted_successful(self):
        return self.wait_visible(self.PROGRESS_MESSAGE)
