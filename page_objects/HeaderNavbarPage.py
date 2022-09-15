from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HeaderNavbarPage(BasePage):
    BUCKET_BUTTON = (By.CSS_SELECTOR, "#cart>.btn")
    SEARCH_FIELD = (By.CSS_SELECTOR, ".input-lg")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-lg")
    ACCOUNT_CHOICE = (By.CSS_SELECTOR, "#top-links .dropdown .fa-user")
    NAVBAR_ELEMENTS = (By.CSS_SELECTOR, ".navbar-nav")
    DESKTOPS = (By.XPATH, "//a[text()='Desktops']")
    LAPTOPS = (By.XPATH, "//a[text()='Laptops & Notebooks']")
    COMPONENTS = (By.XPATH, "//a[text()='Components']")
    MP3 = (By.XPATH, "//a[text()='MP3 Players']")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "i[class='fa fa-caret-down']")
    EURO_SIGN = (By.XPATH, "//strong[text()='€']")
    EURO_BUTTON = (By.CSS_SELECTOR, 'button[name="EUR"]')
    DOLLAR_SIGN = (By.XPATH, "//strong[text()='$']")
    DOLLAR_BUTTON = (By.CSS_SELECTOR, 'button[name="USD"]')
    STERLING_SIGN = (By.XPATH, "//strong[text()='£']")
    STERLING_BUTTON = (By.CSS_SELECTOR, 'button[name="GBP"]')

    def check_search_elements_exists(self):
        self.waiter(3).until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        self.driver.find_element(*self.SEARCH_FIELD)
        self.driver.find_element(*self.SEARCH_BUTTON)

    def check_head_nav_elements(self):
        self.driver.find_element(*self.BUCKET_BUTTON)
        self.driver.find_element(*self.ACCOUNT_CHOICE)
        self.driver.find_element(*self.NAVBAR_ELEMENTS)
        self.driver.find_element(*self.DESKTOPS)
        self.driver.find_element(*self.LAPTOPS)
        self.driver.find_element(*self.COMPONENTS)
        self.driver.find_element(*self.MP3)

    def switching_to_dollar(self):
        self.driver.find_element(*self.CURRENCY_DROPDOWN).click()
        self.driver.find_element(*self.DOLLAR_BUTTON).click()
        self.driver.find_element(*self.DOLLAR_SIGN)

    def switching_to_euro(self):
        self.driver.find_element(*self.CURRENCY_DROPDOWN).click()
        self.driver.find_element(*self.EURO_BUTTON).click()
        self.driver.find_element(*self.EURO_SIGN)

    def switching_to_pound(self):
        self.driver.find_element(*self.CURRENCY_DROPDOWN).click()
        self.driver.find_element(*self.STERLING_BUTTON).click()
        self.driver.find_element(*self.STERLING_SIGN)
