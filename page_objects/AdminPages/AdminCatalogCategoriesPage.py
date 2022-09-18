from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminCatalogCategoriesPage(BasePage):
    ADD_NEW = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')

