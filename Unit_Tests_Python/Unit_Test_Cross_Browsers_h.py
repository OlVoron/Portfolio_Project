from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import helpers as h


class DATChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_dat_chrome(self):
        driver = self.driver
        driver.get(h.main_url)
        driver.maximize_window()
        h.delay()

        # Check API response code
        h.check_api_code(driver)

        # Verify title of home page
        h.verify_title_home_page(driver)

        # Verify DAT logo
        h.verify_dat_logo(driver)

        #  Verify header
        h.verify_header_dat(driver)

        # Verify functionality of "Products" menu in header
        h.verify_products_headers(driver)

        # Verify functionality of "Solutions" menu in header
        h.verify_solutions_headers(driver)

        # Verify functionality of "Resources" menu in header
        h.verify_resources_header(driver)

        # Verify functionality of "Contact" menu in header
        h.verify_contact_header(driver)

        # Verify functionality of "Search" menu in header
        h.verify_search_header(driver)

        # Verify functionality of "Login" menu in header
        h.verify_login_header(driver)

        # Verify functionality of "Signup" menu in header
        h.verify_signup_header(driver)

    def tearDown(self):
        self.driver.quit()


class DATFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_dat_firefox(self):
        driver = self.driver
        driver.get(h.main_url)
        driver.maximize_window()
        h.delay()

        # Check API response code
        h.check_api_code(driver)

        # Verify title of home page
        h.verify_title_home_page(driver)

        # Verify DAT logo
        h.verify_dat_logo(driver)

        #  Verify header
        h.verify_header_dat(driver)

        # Verify functionality of "Products" menu in header
        h.verify_products_headers(driver)

        # Verify functionality of "Solutions" menu in header
        h.verify_solutions_headers(driver)

        # Verify functionality of "Resources" menu in header
        h.verify_resources_header(driver)

        # Verify functionality of "Contact" menu in header
        h.verify_contact_header(driver)

        # Verify functionality of "Search" menu in header
        h.verify_search_header(driver)

        # Verify functionality of "Login" menu in header
        h.verify_login_header(driver)

        # Verify functionality of "Signup" menu in header
        h.verify_signup_header(driver)

    def tearDown(self):
        self.driver.quit()


class DATEdge(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_dat_edge(self):
        driver = self.driver
        driver.get(h.main_url)
        driver.maximize_window()
        h.delay()

        # Check API response code
        h.check_api_code(driver)

        # Verify title of home page
        h.verify_title_home_page(driver)

        # Verify DAT logo
        h.verify_dat_logo(driver)

        #  Verify header
        h.verify_header_dat(driver)

        # Verify functionality of "Products" menu in header
        h.verify_products_headers(driver)

        # Verify functionality of "Solutions" menu in header
        h.verify_solutions_headers(driver)

        # Verify functionality of "Resources" menu in header
        h.verify_resources_header(driver)

        # Verify functionality of "Contact" menu in header
        h.verify_contact_header(driver)

        # Verify functionality of "Search" menu in header
        h.verify_search_header(driver)

        # Verify functionality of "Login" menu in header
        h.verify_login_header(driver)

        # Verify functionality of "Signup" menu in header
        h.verify_signup_header(driver)

    def tearDown(self):
        self.driver.quit()
