def test_head_nav(head_nav, driver):
    head_nav = head_nav(driver)
    head_nav.check_search_elements_exists()
    head_nav.check_head_nav_elements()


def test_product_card(driver, product_cards):
    product_cards = product_cards(driver)
    product_cards.check_elements_exists()


def test_login_to_admin_page(driver, admin_page, urls):
    driver.base_url += urls.ADMIN_ENDPOINT
    admin_page = admin_page(driver)
    admin_page.check_elements_exists()
    admin_page.log_in_to_admin()


def test_add_product_in_admin_page(driver, admin_page, urls, admin_dashboard_page, admin_product_page):
    driver.base_url += urls.ADMIN_ENDPOINT
    admin_page = admin_page(driver)
    admin_page.log_in_to_admin()
    driver.base_url = driver.current_url
    admin_dashboard_page = admin_dashboard_page(driver)
    admin_dashboard_page.go_to_the_products()
    driver.base_url = driver.current_url
    admin_product_page = admin_product_page(driver)
    admin_product_page.add_new_product()
    admin_product_page.check_added_product()
    assert admin_product_page.product_count == 1


def test_delete_product_in_admin_page(driver, admin_page, urls, admin_dashboard_page, admin_product_page):
    driver.base_url += urls.ADMIN_ENDPOINT
    admin_page = admin_page(driver)
    admin_page.log_in_to_admin()
    driver.base_url = driver.current_url
    admin_dashboard_page = admin_dashboard_page(driver)
    admin_dashboard_page.go_to_the_products()
    driver.base_url = driver.current_url
    admin_product_page = admin_product_page(driver)
    admin_product_page.delete_product()


def test_user_registration_page(driver, urls, registration_page):
    driver.base_url += urls.REGISTRATION_ENDPOINT
    registration_page = registration_page(driver)
    registration_page.check_elements_exists()
    registration_page.register_new_user()


def test_switching_the_currency(head_nav, driver):
    head_nav = head_nav(driver)
    head_nav.switching_to_dollar()
    head_nav.switching_to_euro()
