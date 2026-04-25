import allure

from page_objects.registration_page import Registration


@allure.title("Check registration page required elements")
@allure.description("Check that required elements are visible on registration page")
def test_elements_is_visible_on_registration_page(driver, prestashop_base_url):
    registration = Registration(driver)

    with allure.step("Open registration page"):
        registration.open(prestashop_base_url)

    with allure.step("Check required elements visible on registration page"):
        registration.check_required_elements_visible()
