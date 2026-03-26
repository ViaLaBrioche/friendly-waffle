from page_objects.catalog_page import CatalogPage


def test_elements_is_visible_on_catalog_page(driver, prestashop_base_url):
    catalog = CatalogPage(driver)
    catalog.open(prestashop_base_url)
    catalog.check_required_elements_visible()
