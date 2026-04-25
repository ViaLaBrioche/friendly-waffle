import allure

from page_objects.main_page import MainPage


@allure.title("Check main page required elements")
@allure.description("Check that required elements are visible on main page")
def test_elements_is_visible_on_main_page(driver, prestashop_base_url):
    main = MainPage(driver)

    with allure.step("Open main page"):
        main.open(prestashop_base_url)

    with allure.step("Check required elements visible on main page"):
        main.check_required_elements_visible()
