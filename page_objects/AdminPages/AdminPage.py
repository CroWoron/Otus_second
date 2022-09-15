from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    BACK_MAIN_MENU_LINK = (By.CSS_SELECTOR, ".navbar-brand")
    ADMIN_USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    ADMIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    ADMIN_PASSWORD_RECOVER = (By.CSS_SELECTOR, ".help-block")
    ADMIN_LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")

    def check_elements_exists(self):
        self.driver.find_element(*self.BACK_MAIN_MENU_LINK)
        self.driver.find_element(*self.ADMIN_USERNAME_FIELD)
        self.driver.find_element(*self.ADMIN_PASSWORD_FIELD)
        self.driver.find_element(*self.ADMIN_PASSWORD_RECOVER)
        self.driver.find_element(*self.ADMIN_LOGIN_BUTTON)

    def log_in_to_admin(self):
        self.driver.find_element(*self.ADMIN_USERNAME_FIELD).send_keys('user')
        self.driver.find_element(*self.ADMIN_PASSWORD_FIELD).send_keys('bitnami')
        self.driver.find_element(*self.ADMIN_LOGIN_BUTTON).click()

    def add_new_product(self):
        pass

    def delete_product(self):
        pass