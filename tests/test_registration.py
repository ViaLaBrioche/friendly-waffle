from page_objects.registration_page import Registration


def test_elements_is_visible_on_registration_page(driver, prestashop_base_url):
    registration = Registration(driver)
    registration.open(prestashop_base_url)
    registration.check_required_elements_visible()
