from page_objects.admin_login_page import AdminLoginPage


def test_elements_is_visible_on_admin_login_page(driver, prestashop_admin_url):
    admin_login_page = AdminLoginPage(driver)
    admin_login_page.open(prestashop_admin_url)
    admin_login_page.check_required_elements_visible()
