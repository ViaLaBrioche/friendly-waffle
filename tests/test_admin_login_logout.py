import allure

from page_objects.admin_login_page import AdminLoginPage


@allure.title("Login and sign out in admin panel")
@allure.description("Check that admin user can log in and sign out")
def test_admin_login_page_elements(driver, prestashop_admin_url, admin_user):
    admin_login_page = AdminLoginPage(driver)

    with allure.step("Open admin login page"):
        admin_login_page.open(prestashop_admin_url)

    with allure.step("Wait until admin login page loaded"):
        admin_login_page.wait_until_loaded_login_page()

    with allure.step("Login as admin user"):
        admin_login_page.login(admin_user["email"], admin_user["password"])

    with allure.step("Check that admin user is logged in"):
        assert admin_login_page.is_logged_in()

    with allure.step("Open admin profile menu"):
        admin_login_page.open_profile()

    with allure.step("Sign out from admin panel"):
        admin_login_page.sign_out()

    with allure.step("Wait until admin login page loaded after sign out"):
        admin_login_page.wait_until_loaded_login_page()
