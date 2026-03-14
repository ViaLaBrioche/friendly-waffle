from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_main_page(wait):
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="login-content-card"]')
        ),
        message="Не появился элемент c id (#login-content-card)",
    )

    wait.until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#login-header")),
        message="Не появился элемент с id (#login-header)",
    )

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//button[contains(., "Log in")]')
        ),
        message="Не появилась кнопка с контентом (Log in)",
    )


def test_admin_login_page_elements(driver, prestashop_admin_url):
    driver.get(prestashop_admin_url)
    wait = WebDriverWait(driver, 10)

    wait_main_page(wait)

    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("admin@example.com")
    driver.find_element(By.CSS_SELECTOR, "#passwd").send_keys("Admin123!")
    driver.find_element(By.CSS_SELECTOR, "#submit_login").click()

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//li[@id="employee_infos"]')
        ),
        message="Не появился элемент с классом (#employee_infos)",
    )

    assert driver.find_element(By.XPATH, '//li[@id="employee_infos"]').is_displayed()

    driver.find_element(By.XPATH, '//li[@id="employee_infos"]').click()

    wait.until(
        method=EC.visibility_of_element_located((By.XPATH, '//a[@id="header_logout"]')),
        message="Не появился элемент с id (#header_logout)",
    )

    driver.find_element(By.XPATH, '//a[@id="header_logout"]').click()

    wait_main_page(wait)
