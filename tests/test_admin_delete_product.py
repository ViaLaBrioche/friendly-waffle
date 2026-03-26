from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_products_page import AdminProductsPage


def test_admin_delete_product(driver, prestashop_admin_url, admin_user):
    admin_products_page = AdminProductsPage(driver)
    admin_login_page = AdminLoginPage(driver)
    admin_products_page.open(prestashop_admin_url)
    admin_login_page.login(admin_user["email"], admin_user["password"])
    admin_products_page.wait_until_loaded()
    admin_products_page.choose_product()
    admin_products_page.open_actions()
    admin_products_page.delete_product()
    admin_products_page.confirm_delete_product()
    assert admin_products_page.wait_deleted_successful()
