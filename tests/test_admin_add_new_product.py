import allure

from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_products_page import AdminProductsPage


@allure.title("Add new product in admin panel")
@allure.description("Check that admin can add a new product")
def test_admin_add_new_product(driver, prestashop_admin_url, admin_user, product_data):
    admin_products_page = AdminProductsPage(driver)
    admin_login_page = AdminLoginPage(driver)

    with allure.step("Open admin products page"):
        admin_products_page.open(prestashop_admin_url)

    with allure.step("Login as admin user"):
        admin_login_page.login(admin_user["email"], admin_user["password"])

    with allure.step("Wait until admin products page loaded"):
        admin_products_page.wait_until_loaded()

    with allure.step("Open add new product page"):
        admin_products_page.add_new_product_main_page()

    with allure.step("Select standard product type"):
        admin_products_page.select_standard_product()

    with allure.step("Enter product name"):
        admin_products_page.enter_product_name(product_data["name"])

    with allure.step("Enter product description"):
        admin_products_page.enter_product_description(product_data["description"])

    with allure.step("Save product"):
        admin_products_page.save_product()
