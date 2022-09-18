import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_objects.HeaderNavbarPage import HeaderNavbarPage
from page_objects.ProductCards import ProductCards
from page_objects.AdminPages.AdminPage import AdminPage
from page_objects.AdminPages.AdminDashboardPage import AdminDashboardPage
from page_objects.AdminPages.AdminProductPage import AdminProductPage
from page_objects.RegistrationPage import RegistrationPage
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
    if base_url == 'admin':
        base_url = Urls.BASE_URL+Urls.ADMIN_ENDPOINT
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
def head_nav():
    return HeaderNavbarPage


@pytest.fixture
def product_cards():
    return ProductCards


@pytest.fixture
def admin_page():
    return AdminPage

@pytest.fixture
def admin_dashboard_page():
    return AdminDashboardPage

@pytest.fixture
def admin_product_page():
    return AdminProductPage

@pytest.fixture
def registration_page():
    return RegistrationPage


@pytest.fixture
def urls():
    return Urls
