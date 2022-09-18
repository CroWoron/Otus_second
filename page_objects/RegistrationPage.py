from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.test_data import TestData


class RegistrationPage(BasePage):
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    SUBSCRIBE_RADIO_BUTTONS = (By.CSS_SELECTOR, "input[type=radio]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    POLICY_CHECK_BOX = (By.CSS_SELECTOR, "input[type=checkbox]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type=submit]")
    TELEPHONE_FIELD = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-confirm")
    CHECK_BOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")
    ACCOUNT_SUCCESS = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")

    def check_elements_exists(self):
        self.driver.find_element(*self.FIRST_NAME_FIELD)
        self.driver.find_element(*self.LAST_NAME_FIELD)
        self.driver.find_elements(*self.SUBSCRIBE_RADIO_BUTTONS)
        self.waiter(3).until(EC.element_to_be_clickable(self.POLICY_CHECK_BOX))
        self.driver.find_element(*self.POLICY_CHECK_BOX)
        self.driver.find_element(*self.CONTINUE_BUTTON)

    def register_new_user(self):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(TestData.MAIN_NAME)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(TestData.LAST_NAME)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(TestData.EMAIL)
        self.driver.find_element(*self.TELEPHONE_FIELD).send_keys(TestData.PHONE)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(TestData.PASSWORD)
        self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD).send_keys(TestData.PASSWORD)
        self.driver.find_element(*self.CHECK_BOX).click()
        self.driver.find_element(*self.BUTTON_SUBMIT).click()
        self.driver.find_element(*self.ACCOUNT_SUCCESS)
