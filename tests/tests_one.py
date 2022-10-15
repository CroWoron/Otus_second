import allure
import pytest


@allure.title('Проверка навигации')
def test_head_nav(head_nav, browser):
    with allure.step('Проверка наличия элементов навигации'):
        head_nav = head_nav(browser)
        head_nav.check_search_elements_exists()
    with allure.step('Проверка элементов хедера'):
        head_nav.check_head_nav_elements()


@allure.title('Карточка продукта')
def test_product_card(browser, product_cards):
    with allure.step('Проверка наличия элементов'):
        product_cards = product_cards(browser)
        product_cards.check_elements_exists()


@allure.title('Вход на страницу администратора')
def test_login_to_admin_page(browser, admin_page, urls):
    with allure.step('Проверка наличия элементов'):
        browser.base_url += urls.ADMIN_ENDPOINT
        admin_page = admin_page(browser)
        admin_page.check_elements_exists()
    with allure.step('Вход'):
        admin_page.log_in_to_admin()


@allure.title('Добавление продукта на странице администратора')
def test_add_product_in_admin_page(browser, admin_page, urls, admin_dashboard_page, admin_product_page):
    with allure.step('Вход'):
        browser.base_url += urls.ADMIN_ENDPOINT
        admin_page = admin_page(browser)
        admin_page.log_in_to_admin()
        browser.base_url = browser.current_url
    with allure.step('Переход в меню добавления'):
        admin_dashboard_page = admin_dashboard_page(browser)
        admin_dashboard_page.go_to_the_products()
        browser.base_url = browser.current_url
    with allure.step('Добавление нового продукта'):
        admin_product_page = admin_product_page(browser)
        admin_product_page.add_new_product()
        admin_product_page.check_added_product()
        assert admin_product_page.product_count == 1


@allure.title('Удаление продукта со страницы')
def test_delete_product_in_admin_page(browser, admin_page, urls, admin_dashboard_page, admin_product_page):
    with allure.step('Вход'):
        browser.base_url += urls.ADMIN_ENDPOINT
        admin_page = admin_page(browser)
        admin_page.log_in_to_admin()
    with allure.step('Переход в меню продуктовв'):
        browser.base_url = browser.current_url
        admin_dashboard_page = admin_dashboard_page(browser)
        admin_dashboard_page.go_to_the_products()
    with allure.step('Удаление продукта'):
        browser.base_url = browser.current_url
        admin_product_page = admin_product_page(browser)
        admin_product_page.delete_product()


@allure.title('регистрация пользователя')
@pytest.mark.skip('Пользователь зарегистрирован')
def test_user_registration_page(browser, urls, registration_page):
    with allure.step('Проверка наличия элементов'):
        browser.base_url += urls.REGISTRATION_ENDPOINT
        registration_page = registration_page(browser)
        registration_page.check_elements_exists()
    with allure.step('Регистрация пользователя'):
        registration_page.register_new_user()


@allure.title('Переключение валюты')
def test_switching_the_currency(head_nav, browser):
    head_nav = head_nav(browser)
    with allure.step('Переключение на доллары'):
        head_nav.switching_to_dollar()
    with allure.step('Переключение на евро'):
        head_nav.switching_to_euro()
    with allure.step('Переключение на фунт'):
        head_nav.switching_to_pound
