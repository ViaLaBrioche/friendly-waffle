from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random


def test_elements_is_visible_on_admin_login_page(driver, prestashop_base_url):
    driver.get(prestashop_base_url)
    wait = WebDriverWait(driver, 10)

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="products row"]')
        ),
        message="Не появился класс с контентом (.products row)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//h2[normalize-space()="Sample 1"]')
        ),
        message="Не появился элемент с контентом (Sample 1)",
    )

    random_product_id = random.randint(1, 8)

    product = driver.find_element(
        By.XPATH, f'//article[@data-id-product="{random_product_id}"]'
    )

    product_name = product.find_element(
        By.XPATH, './/h3[@class="h3 product-title"]/a'
    ).text

    product.click()

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//button[contains(., "Add to cart")]')
        ),
        message="Не появилась кнопка с контентом (Add to cart)",
    )

    driver.find_element(By.XPATH, '//button[contains(., "Add to cart")]').click()

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//a[contains(., "Proceed to checkout")]')
        ),
        message="Не появилась кнопка с контентом (Proceed to checkout)",
    )

    driver.find_element(By.XPATH, '//a[contains(., "Proceed to checkout")]').click()

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//h1[normalize-space()="Shopping Cart"]')
        ),
        message="Не появилась кнопка с контентом (Add to cart)",
    )

    product_name_cart = driver.find_element(
        By.XPATH, './/div[@class="product-line-info"]/a'
    ).text

    assert product_name.lower().replace("...", "") in product_name_cart.lower()
