import os
import pytest
import datetime
import allure
import logging

from faker import Faker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):

    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--browser_version", action="store", default="120.0")
    parser.addoption("--executor", action="store", default="local")

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


@pytest.fixture
def prestashop_admin_url(request):
    return request.config.getoption("--prestashop_administration")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    browser_version = request.config.getoption("--browser_version")
    executor = request.config.getoption("--executor")

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(request.node.name)
    logger.handlers.clear()
    logger.setLevel(log_level)

    file_handler = logging.FileHandler(f"logs/{request.node.name}.log", mode="w")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)

    logger.info("===> Test started at %s", datetime.datetime.now())

    browser = None

    if executor == "selenoid":
        if browser_name == "chrome":
            options = ChromeOptions()

        elif browser_name == "firefox":
            options = FirefoxOptions()

        else:
            raise ValueError(f"Unsupported browser for selenoid: {browser_name}")

        options.set_capability("browserVersion", browser_version)

        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": False,
            },
        )

        browser = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub",
            options=options,
        )

    elif browser_name == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        browser = webdriver.Firefox(options=options)

    elif browser_name == "chrome":
        options = ChromeOptions()

        options.binary_location = "/usr/bin/chromium"

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")

        service = ChromeService(executable_path="/usr/bin/chromedriver")
        browser = webdriver.Chrome(service=service, options=options)

    elif browser_name == "yandex":
        service = ChromeService(
            executable_path="/Users/andreikapaev/Downloads/yandexdriver"
        )

        options = ChromeOptions()
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
        browser = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    browser.log_level = log_level
    browser.logger = logger
    browser.test_name = request.node.name

    logger.info("Browser %s started", browser_name)

    yield browser

    browser.quit()

    logger.info("===> Test finished at %s", datetime.datetime.now())

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
    return {
        "email": "admin@example.com",
        "password": "Admin123!",
    }


@pytest.fixture
def product_data():
    fake = Faker()

    return {
        "name": fake.word(),
        "description": fake.text(max_nb_chars=50),
    }


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
