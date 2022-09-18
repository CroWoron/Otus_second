from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AdminDashboardPage(BasePage):
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS = (By.XPATH, "//a[text()='Products']")

    def go_to_the_products(self):
        self.driver.find_element(*self.MENU_CATALOG).click()
        self.waiter(5).until(EC.element_to_be_clickable(self.PRODUCTS))
        self.driver.find_element(*self.PRODUCTS).click()


