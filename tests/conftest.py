import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.locators import MainPageLocators, CatalogPageLocators, ProductCartLocators, AdminPageLocators, \
    RegistrationPageLocators
from src.urls import Urls


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="chose web-driver"
    )
    parser.addoption(
        "--base_url", default=Urls.BASE_URL, help="insert url"
    )
    parser.addoption(
        "--drivers", default=os.path.expanduser('~/Desktop/otus/web_drivers'), help='set webdriwers path'
    )


@pytest.fixture
def driver(request):
    name_of_browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    drivers = request.config.getoption("--drivers")
    if name_of_browser == 'chrome':
        service = Service(executable_path=os.path.join(drivers, 'chromedriver'))
        _driver = webdriver.Chrome(service=service)
    elif name_of_browser == 'firefox':
        _driver = webdriver.Firefox(executable_path=os.path.join(drivers, 'geckodriver'))
    elif name_of_browser == 'opera':
        _driver = webdriver.Opera(os.path.join(drivers, 'opera'))
    _driver.base_url = base_url
    yield _driver
    _driver.quit()


@pytest.fixture
def main_page_locators():
    return MainPageLocators


@pytest.fixture
def catalog_page_locator():
    return CatalogPageLocators


@pytest.fixture
def product_card_locator():
    return ProductCartLocators


@pytest.fixture
def admin_page_locators():
    return AdminPageLocators


@pytest.fixture
def registration_page_locators():
    return RegistrationPageLocators


@pytest.fixture
def urls():
    return Urls
