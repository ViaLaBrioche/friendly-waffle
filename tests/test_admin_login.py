from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_elements_is_visible_on_admin_login_page(driver, prestashop_admin_url):
    driver.get(prestashop_admin_url)
    wait = WebDriverWait(driver, 10)

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
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="form-group"]')
        ),
        message="Не появился класс с контентом (.form-group)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="login-footer"]')
        ),
        message="Не появился элемент с id (#login-footer)",
    )
