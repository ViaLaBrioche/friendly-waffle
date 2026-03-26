import pytest
from page_objects.registration_page import Registration


@pytest.mark.parametrize("gender", ["mr", "mrs"])
def test_registration_new_user(
    gender, driver, registration_user_data, prestashop_base_url
):
    registration = Registration(driver)
    registration.open(prestashop_base_url)
    registration.wait_until_loaded()
    registration.select_social_title(gender)
    registration.enter_first_name(registration_user_data["first_name"])
    registration.enter_last_name(registration_user_data["last_name"])
    registration.enter_email(registration_user_data["email"])
    registration.enter_password(registration_user_data["password"])
    registration.enter_birthdate(registration_user_data["birth_date"])
    registration.set_i_agree()
    registration.set_newsletter()
    registration.set_customer_privacy()
    registration.save_information()
