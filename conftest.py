import pytest
import datetime
import allure
import logging
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

    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def prestashop_base_url(request):
    return request.config.getoption("--prestashop")


@pytest.fixture()
def prestashop_admin_url(request):
    return request.config.getoption("--prestashop_administration")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")

    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log", mode="w")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test started at %s" % datetime.datetime.now())

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

    browser.log_level = log_level
    browser.logger = logger
    browser.test_name = request.node.name
    logger.info("Browser %s started" % browser_name)

    yield browser

    browser.quit()
    logger.info("===> Test finished at %s" % datetime.datetime.now())
    file_handler.close()

    logger.removeHandler(file_handler)


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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )
