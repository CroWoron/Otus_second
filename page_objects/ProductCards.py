from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductCards(BasePage):
    PRODUCT_CART = (By.CSS_SELECTOR, ".product-thumb")
    CART_IMAGE = (By.CSS_SELECTOR, "img")
    CART_PRICE = (By.CSS_SELECTOR, ".price")
    CART_TAX = (By.CSS_SELECTOR, ".price-tax")
    CART_BUTTONS = (By.CSS_SELECTOR, "button")

    def check_elements_exists(self):
        cart = self.driver.find_element(*self.PRODUCT_CART)
        cart.find_element(*self.CART_IMAGE)
        cart.find_element(*self.CART_PRICE)
        cart.find_element(*self.CART_TAX)


