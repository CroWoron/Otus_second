import time

from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.test_data import TestData


class AdminProductPage(BasePage):
    ADD_BUTTON = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA = (By.XPATH, "//a[text()='Data']")
    MODEL = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')
    FILTER_PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name')
    FILTER_BUTTON = (By.CSS_SELECTOR, '#button-filter')
    PRODUCT_PANEL = (By.CSS_SELECTOR, 'tbody tr')
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    NO_RESULT_MESSAGE = (By.XPATH, "//td[text()='No results!']")
    product_count = None

    def add_new_product(self):
        self.driver.find_element(*self.ADD_BUTTON).click()
        self.driver.find_element(*self.PRODUCT_NAME).send_keys(TestData.MAIN_NAME)
        self.driver.find_element(*self.META_TAG_TITLE).send_keys(TestData.DESCRIPTION)
        self.driver.find_element(*self.DATA).click()
        self.waiter(5).until(EC.element_to_be_clickable(self.MODEL))
        self.driver.find_element(*self.MODEL).send_keys(TestData.ATTRIBUTE)
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def check_added_product(self):
        self.driver.find_element(*self.FILTER_PRODUCT_NAME).send_keys(TestData.MAIN_NAME)
        self.driver.find_element(*self.MODEL).send_keys(TestData.ATTRIBUTE)
        self.driver.find_element(*self.FILTER_BUTTON).click()
        panel = self.driver.find_elements(*self.PRODUCT_PANEL)
        self.product_count = len(panel)

    def delete_product(self):
        self.driver.find_element(*self.FILTER_PRODUCT_NAME).send_keys(TestData.MAIN_NAME)
        self.driver.find_element(*self.MODEL).send_keys(TestData.ATTRIBUTE)
        self.driver.find_element(*self.FILTER_BUTTON).click()
        self.driver.find_elements(*self.PRODUCT_CHECKBOX)[1].click()
        self.driver.find_element(*self.DELETE_BUTTON).click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(*self.NO_RESULT_MESSAGE)
