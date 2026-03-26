from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_elements_is_visible_on_main_page(driver, prestashop_base_url):
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
    wait.until(
        method=EC.visibility_of_element_located((By.XPATH, '//*[@id="header"]')),
        message="Не появился элемент с id (#header)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="content"]/a[@class="banner"]')
        ),
        message="Не появился класс с контентом (.banner)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="footer-container"]')
        ),
        message="Не появился класс с контентом (.footer-container)",
    )
