from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.driver.base_url)

    def waiter(self, sec):
        waiter = WebDriverWait(self.driver, sec)
        return waiter
