import allure
import pytest


@allure.title('Navigator checking')
def test_head_nav(head_nav, browser):
    with allure.step('this is step to your face'):
        head_nav = head_nav(browser)
        head_nav.check_search_elements_exists()
    with allure.step('ant this too much'):
        head_nav.check_head_nav_elements()


def test_product_card(browser, product_cards):
    product_cards = product_cards(browser)
    product_cards.check_elements_exists()


def test_login_to_admin_page(browser, admin_page, urls):
    browser.base_url += urls.ADMIN_ENDPOINT
    admin_page = admin_page(browser)
    admin_page.check_elements_exists()
    admin_page.log_in_to_admin()


def test_add_product_in_admin_page(browser, admin_page, urls, admin_dashboard_page, admin_product_page):
    browser.base_url += urls.ADMIN_ENDPOINT
    admin_page = admin_page(browser)
    admin_page.log_in_to_admin()
    browser.base_url = browser.current_url
    admin_dashboard_page = admin_dashboard_page(browser)
    admin_dashboard_page.go_to_the_products()
    browser.base_url = browser.current_url
    admin_product_page = admin_product_page(browser)
    admin_product_page.add_new_product()
    admin_product_page.check_added_product()
    assert admin_product_page.product_count == 1


def test_delete_product_in_admin_page(browser, admin_page, urls, admin_dashboard_page, admin_product_page):
    browser.base_url += urls.ADMIN_ENDPOINT
    admin_page = admin_page(browser)
    admin_page.log_in_to_admin()
    browser.base_url = browser.current_url
    admin_dashboard_page = admin_dashboard_page(browser)
    admin_dashboard_page.go_to_the_products()
    browser.base_url = browser.current_url
    admin_product_page = admin_product_page(browser)
    admin_product_page.delete_product()


@pytest.mark.skip('The user is already registered')
def test_user_registration_page(browser, urls, registration_page):
    browser.base_url += urls.REGISTRATION_ENDPOINT
    registration_page = registration_page(browser)
    registration_page.check_elements_exists()
    registration_page.register_new_user()


def test_switching_the_currency(head_nav, browser):
    head_nav = head_nav(browser)
    head_nav.switching_to_dollar()
    head_nav.switching_to_euro()
