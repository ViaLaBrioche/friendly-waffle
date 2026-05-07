import allure

from page_objects.admin_login_page import AdminLoginPage


@allure.title("Check admin login page required elements")
@allure.description("Check that required elements are visible on admin login page")
def test_elements_is_visible_on_admin_login_page(driver, prestashop_admin_url):
    admin_login_page = AdminLoginPage(driver)

    with allure.step("Open admin login page"):
        admin_login_page.open(prestashop_admin_url)

    with allure.step("Check required elements visible on admin login page"):
        admin_login_page.check_required_elements_visible()
