# tests/test_registration.py

import allure
import pytest

from page_objects.main_page import MainPage
from page_objects.registration_page import Registration


@allure.title("Register new user")
@allure.description("Check registration new user")
@pytest.mark.parametrize("gender", ["mr", "mrs"], ids=["mr", "mrs"])
def test_registration_new_user(
    gender, driver, registration_user_data, prestashop_base_url
):
    main = MainPage(driver)
    registration = Registration(driver)

    with allure.step("Open registration page"):
        registration.open(prestashop_base_url)

    with allure.step("Wait until registration page loaded"):
        registration.wait_until_loaded()

    with allure.step(f"Select social title: {gender}"):
        registration.select_social_title(gender)

    with allure.step("Enter first name"):
        registration.enter_first_name(registration_user_data["first_name"])

    with allure.step("Enter last name"):
        registration.enter_last_name(registration_user_data["last_name"])

    with allure.step("Enter email"):
        registration.enter_email(registration_user_data["email"])

    with allure.step("Enter password"):
        registration.enter_password(registration_user_data["password"])

    with allure.step("Enter birth date"):
        registration.enter_birthdate(registration_user_data["birth_date"])

    with allure.step("Accept terms and conditions"):
        registration.set_i_agree()

    with allure.step("Subscribe to newsletter"):
        registration.set_newsletter()

    with allure.step("Accept customer privacy"):
        registration.set_customer_privacy()

    with allure.step("Save registration form"):
        registration.save_information()

    with allure.step("Check main page required elements visible after registration"):
        main.check_required_elements_visible()
