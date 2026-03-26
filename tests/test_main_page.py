from page_objects.main_page import MainPage


def test_elements_is_visible_on_main_page(driver, prestashop_base_url):
    main = MainPage(driver)
    main.open(prestashop_base_url)
    main.check_required_elements_visible()
