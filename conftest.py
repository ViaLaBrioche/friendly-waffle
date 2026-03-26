import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from faker import Faker


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

    parser.addoption(
        "--prestashop",
        action="store",
        default="http://localhost:8081",
    )

    parser.addoption(
        "--prestashop_administration",
        action="store",
        default="http://localhost:8081/administration",
    )


@pytest.fixture
def prestashop_base_url(request):
    return request.config.getoption("--prestashop")


@pytest.fixture()
def prestashop_admin_url(request):
    return request.config.getoption("--prestashop_administration")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "firefox":
        browser = webdriver.Firefox()
    elif browser_name == "chrome":
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)
    elif browser_name == "yandex":
        service = ChromeService(
            executable_path="/Users/andreikapaev/Downloads/yandexdriver"
        )
        options = ChromeOptions()
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
        browser = webdriver.Chrome(service=service, options=options)

    yield browser

    browser.quit()


@pytest.fixture
def registration_user_data():
    fake = Faker()

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=12),
        "birth_date": "01/01/2000",
    }


@pytest.fixture
def admin_user():
    return {"email": "admin@example.com", "password": "Admin123!"}


@pytest.fixture
def product_data():
    fake = Faker()

    return {"name": fake.word(), "description": fake.text(max_nb_chars=50)}
