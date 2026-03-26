from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_change_currency_main_page(driver, prestashop_base_url):
    driver.get(prestashop_base_url)
    assert driver.title == "PrestaShop"
    wait = WebDriverWait(driver, 10)

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//img[@class="logo img-fluid"]')
        ),
        message="Не появился класс с контентом (.logo img-fluid)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//h2[normalize-space()="Sample 1"]')
        ),
        message="Не появился элемент с контентом (Sample 1)",
    )

    def check_currency(driver):
        currency_set = driver.find_element(
            By.XPATH, '//span[@class="expand-more _gray-darker"]'
        ).text
        currency_product = driver.find_element(By.XPATH, '//span[@class="price"]').text
        assert currency_product.strip()[0] == currency_set.split()[-1]

    check_currency(driver)

    driver.find_element(By.XPATH, '//span[@class="expand-more _gray-darker"]').click()

    wait.until(
        method=EC.visibility_of_element_located((By.XPATH, '//a[@title="US Dollar"]')),
        message="Не появился элемент с контентом (US Dollar)",
    )

    driver.find_element(By.XPATH, '//a[@title="US Dollar"]').click()

    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//span[@class="price"]'), "$")
    )

    check_currency(driver)
