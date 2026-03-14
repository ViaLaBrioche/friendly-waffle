from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_elements_is_visible_on_product_card_page(driver, prestashop_base_url):
    driver.get(f"{prestashop_base_url}/registration")
    wait = WebDriverWait(driver, 10)

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="page-content card card-block"]')
        ),
        message="Не появился класс с контентом (.page-content card card-block)",
    )
    wait.until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#wrapper")),
        message="Не появился элемент с id (#wrapper)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//button[contains(., "Save")]')
        ),
        message="Не появилась кнопка с контентом (Save)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//input[@id="field-firstname"]')
        ),
        message="Не появился элемент с id (#field-firstname)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//input[@id="field-password"]')
        ),
        message="Не появился элемент с id (#field-password)",
    )
