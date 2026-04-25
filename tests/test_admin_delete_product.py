import allure

from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_products_page import AdminProductsPage


@allure.title("Delete product in admin panel")
@allure.description("Check that admin can delete product")
def test_admin_delete_product(driver, prestashop_admin_url, admin_user):
    admin_products_page = AdminProductsPage(driver)
    admin_login_page = AdminLoginPage(driver)

    with allure.step("Open admin products page"):
        admin_products_page.open(prestashop_admin_url)

    with allure.step("Login as admin user"):
        admin_login_page.login(admin_user["email"], admin_user["password"])

    with allure.step("Wait until admin products page loaded"):
        admin_products_page.wait_until_loaded()

    with allure.step("Choose product for delete"):
        admin_products_page.choose_product()

    with allure.step("Open bulk actions menu"):
        admin_products_page.open_actions()

    with allure.step("Delete selected product"):
        admin_products_page.delete_product()

    with allure.step("Confirm delete product"):
        admin_products_page.confirm_delete_product()

    with allure.step("Check product deleted"):
        assert admin_products_page.wait_deleted_successful()
