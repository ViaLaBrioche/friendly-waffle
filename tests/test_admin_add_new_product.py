from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_products_page import AdminProductsPage


def test_admin_add_new_product(driver, prestashop_admin_url, admin_user, product_data):
    admin_products_page = AdminProductsPage(driver)
    admin_login_page = AdminLoginPage(driver)
    admin_products_page.open(prestashop_admin_url)
    admin_login_page.login(admin_user["email"], admin_user["password"])
    admin_products_page.wait_until_loaded()
    admin_products_page.add_new_product_main_page()
    admin_products_page.select_standard_product()
    admin_products_page.enter_product_name(product_data["name"])
    admin_products_page.enter_product_description(product_data["description"])
    admin_products_page.save_product()
