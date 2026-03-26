from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_elements_is_visible_on_catalog_page(driver, prestashop_base_url):
    driver.get(f"{prestashop_base_url}/3-clothes")
    wait = WebDriverWait(driver, 10)

    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="block-categories"]')
        ),
        message="Не появился класс с контентом (.block-categories)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#search_filters_brands")
        ),
        message="Не появился элемент с id (#search_filters_brands)",
    )
    wait.until(
        method=EC.visibility_of_element_located((By.CSS_SELECTOR, "#subcategories")),
        message="Не появился элемент с id (#subcategories)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="block-category card card-block"]')
        ),
        message="Не появился класс с контентом (.block-category card card-block)",
    )
    wait.until(
        method=EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="search_filters"]')
        ),
        message="Не появился элемент с id (#search_filters)",
    )
