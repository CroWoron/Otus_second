from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(driver, main_page_locators, catalog_page_locator):
    wait = WebDriverWait(driver, 3)
    driver.get(driver.base_url)
    driver.find_element(*main_page_locators.BUCKET_BUTTON)
    driver.find_element(*main_page_locators.SEARCH_FIELD)
    wait.until(EC.element_to_be_clickable(main_page_locators.BRANDS_CAROUSEL))
    driver.find_element(*main_page_locators.SEARCH_BUTTON)
    driver.find_element(*main_page_locators.ACCOUNT_CHOICE)
    brands = driver.find_elements(*main_page_locators.BRANDS_CAROUSEL)
    assert len(brands) > 0


def test_catalog_page(driver, catalog_page_locator):
    driver.get(driver.base_url)
    wait = WebDriverWait(driver, 3)
    wait.until(EC.visibility_of_element_located(catalog_page_locator.NAVBAR_ELEMENTS))
    driver.find_element(*catalog_page_locator.NAVBAR_ELEMENTS)
    driver.find_element(*catalog_page_locator.DESKTOPS)
    driver.find_element(*catalog_page_locator.LAPTOPS)
    driver.find_element(*catalog_page_locator.COMPONENTS)
    driver.find_element(*catalog_page_locator.MP3)


def test_product_card(driver, product_card_locator):
    driver.get(driver.base_url)
    cart = driver.find_element(*product_card_locator.PRODUCT_CART)
    cart.find_element(*product_card_locator.CART_IMAGE)
    cart.find_element(*product_card_locator.CART_PRICE)
    cart.find_element(*product_card_locator.CART_TAX)
    buttons = cart.find_elements(*product_card_locator.CART_BUTTONS)
    assert len(buttons) == 3


def test_login_to_admin_page(driver, urls, admin_page_locators):
    driver.get(driver.base_url + urls.ADMIN_ENDPOINT)
    driver.find_element(*admin_page_locators.BACK_MAIN_MENU_LINK)
    driver.find_element(*admin_page_locators.ADMIN_USERNAME_FIELD)
    driver.find_element(*admin_page_locators.ADMIN_PASSWORD_FIELD)
    driver.find_element(*admin_page_locators.ADMIN_PASSWORD_RECOVER)
    driver.find_element(*admin_page_locators.ADMIN_LOGIN_BUTTON)


def test_user_registration_page(driver, urls, registration_page_locators):
    wait = WebDriverWait(driver, 1)
    driver.get(driver.base_url + urls.REGISTRATION_ENDPOINT)
    driver.find_element(*registration_page_locators.FIRST_NAME_FIELD)
    driver.find_element(*registration_page_locators.LAST_NAME_FIELD)
    driver.find_elements(*registration_page_locators.SUBSCRIBE_RADIO_BUTTONS)
    wait.until(EC.element_to_be_clickable(registration_page_locators.POLICY_CHECK_BOX))
    driver.find_element(*registration_page_locators.POLICY_CHECK_BOX)
    driver.find_element(*registration_page_locators.CONTINUE_BUTTON)
