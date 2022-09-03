from selenium.webdriver.common.by import By


class MainPageLocators:
    BUCKET_BUTTON = (By.CSS_SELECTOR, "#cart>.btn")
    SEARCH_FIELD = (By.CSS_SELECTOR, ".input-lg")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-lg")
    ACCOUNT_CHOICE = (By.CSS_SELECTOR, "#top-links .dropdown .fa-user")
    BRANDS_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")


class CatalogPageLocators:
    NAVBAR_ELEMENTS = (By.CSS_SELECTOR, ".navbar-nav")
    DESKTOPS = (By.XPATH, "//a[text()='Desktops']")
    LAPTOPS = (By.XPATH, "//a[text()='Laptops & Notebooks']")
    COMPONENTS = (By.XPATH, "//a[text()='Components']")
    MP3 = (By.XPATH, "//a[text()='MP3 Players']")


class ProductCartLocators:
    PRODUCT_CART = (By.CSS_SELECTOR, ".product-thumb")
    CART_IMAGE = (By.CSS_SELECTOR, "img")
    CART_PRICE = (By.CSS_SELECTOR, ".price")
    CART_TAX = (By.CSS_SELECTOR, ".price-tax")
    CART_BUTTONS = (By.CSS_SELECTOR, "button")


class AdminPageLocators:
    BACK_MAIN_MENU_LINK = (By.CSS_SELECTOR, ".navbar-brand")
    ADMIN_USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    ADMIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    ADMIN_PASSWORD_RECOVER = (By.CSS_SELECTOR, ".help-block")
    ADMIN_LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")


class RegistrationPageLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    SUBSCRIBE_RADIO_BUTTONS = (By.CSS_SELECTOR, "input[type=radio]")
    POLICY_CHECK_BOX = (By.CSS_SELECTOR, "input[type=checkbox]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type=submit]")
