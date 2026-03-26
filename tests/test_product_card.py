from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_elements_is_visible_on_product_card_page(driver, prestashop_base_url):
    driver.get(f"{prestashop_base_url}/2-9-brown-bear-printed-sweater.html#/1-size-s")
    wait = WebDriverWait(driver, 10)

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="product-cover"]/picture')
        ),
        message="Не появился элемент (picture)",
    )
    wait.until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")),
        message="Не появился элемент с id (content)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//button[contains(., "Add to cart")]')
        ),
        message="Не появилась кнопка с контентом (Add to cart)",
    )
    wait.until(
        method=EC.visibility_of_element_located((By.XPATH, '//div[@id="tab-content"]')),
        message="Не появился элемент с id (#tab-content)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="product-comments-list-header"]')
        ),
        message="Не появился элемент с id (#product-comments-list-header)",
    )
