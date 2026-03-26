from page_objects.admin_login_page import AdminLoginPage


def test_admin_login_page_elements(driver, prestashop_admin_url, admin_user):
    admin_login_page = AdminLoginPage(driver)
    admin_login_page.open(prestashop_admin_url)
    admin_login_page.wait_until_loaded_login_page()
    admin_login_page.login(admin_user["email"], admin_user["password"])
    assert admin_login_page.is_logged_in()
    admin_login_page.open_profile()
    admin_login_page.sign_out()
    admin_login_page.wait_until_loaded_login_page()
