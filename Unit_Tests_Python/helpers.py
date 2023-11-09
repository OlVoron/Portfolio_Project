# import helpers as h
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import requests
import time

# URL - home page
main_url = "https://www.dat.com"


def delay():  # Set random delay
    time.sleep(random.randint(1, 3))


def check_api_code(driver):  # Check API response code (403 correct)
    print("DAT Url has", requests.get("https://www.dat.com").status_code, "as status Code")
    code = requests.get("https://www.dat.com").status_code
    if code == 403:
        print("API response code is OK")
    else:
        print("API response code is not 403", "Current code is:", code)


def verify_title_home_page(driver):  # Verify title of home page
    try:
        assert driver.title == "DAT Freight & Analytics - DAT"
        print("The driver title is correct: ", driver.title)
    except AssertionError:
        print("Title is different. Current Title is:", driver.title)


def verify_dat_logo(driver):  # Verify DAT logo
    try:
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='dat-logo']")))
        print("DAT Freight & Analytics logo is visible")
    except TimeoutException:
        print("Logo is loading too much time!")


def verify_header_dat(driver):  # Verify header
    try:
        driver.find_element(By.ID, "menu-item-11327").click()
        driver.find_element(By.ID, "menu-item-12562")
        driver.find_element(By.ID, "menu-item-11326").click()
        driver.find_element(By.ID, "menu-item-12554")
        driver.find_element(By.ID, "menu-item-11328").click()
        driver.find_element(By.ID, "menu-item-12578")
        driver.find_element(By.ID, "menu-item-12842")
        driver.find_element(By.ID, "menu-item-12548")
        driver.find_element(By.ID, "menu-item-12886")
        driver.find_element(By.ID, "menu-item-14352")
        print("Header is correct")
    except NoSuchElementException:
        print("Some title of Header is missing")


def verify_products_headers(driver, h=None):  # Verify functionality of "Products" menu in header
    try:
        driver.find_element(By.ID, "menu-item-11327").click()
        driver.find_element(By.LINK_TEXT, "DAT ONE").click()

        # Verify title of DAT_One page
        try:
            assert driver.title == "DAT One - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11327").click()
        driver.find_element(By.LINK_TEXT, "DAT IQ").click()

        # Verify title of DAT_IQ page
        try:
            assert driver.title == "DAT iQ - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11327").click()
        driver.find_element(By.LINK_TEXT, "SERVICES").click()
        driver.find_element(By.LINK_TEXT, "PRODUCT FINDER").click()
        delay()

        # Verify title of PRODUCTS_FINDER page
        try:
            assert driver.title == "Products - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        print("Submenu of 'Products' is correct")
    except AssertionError:
        print("Submenu of 'Products' is wrong")
        driver.back()


def verify_solutions_headers(driver):  # Verify functionality of "Solutions" menu in header
    try:
        driver.find_element(By.ID, "menu-item-11326").click()
        driver.find_element(By.LINK_TEXT, "CARRIERS").click()

        # Verify title of CARRIERS page
        try:
            assert driver.title == "Trucking Fleet Services - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11326").click()
        driver.find_element(By.LINK_TEXT, "BROKERS").click()

        # Verify title of BROKERS page
        try:
            assert driver.title == "Learn More About DAT Broker Software & Services - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11326").click()
        driver.find_element(By.LINK_TEXT, "SHIPPERS").click()

        # Verify title of SHIPPERS page
        try:
            assert driver.title == "Freight Shippers - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        print("Submenu of 'Solutions' is correct")
    except AssertionError:
        print("Submenu of 'Solutions' is wrong")
        driver.back()


def verify_resources_header(driver):  # Verify functionality of "Resources" menu in header
    try:
        driver.find_element(By.ID, "menu-item-11328").click()
        driver.find_element(By.LINK_TEXT, "TRENDLINES").click()

        # Verify title of TRENDLINES page
        try:
            assert driver.title == "Trucking Industry Trends - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11328").click()
        driver.find_element(By.LINK_TEXT, "BLOG").click()

        # Verify title of BLOG page
        try:
            assert driver.title == "DAT Freight & Analytics - Blog"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11328").click()
        driver.find_element(By.LINK_TEXT, "START-UP GUIDES").click()
        delay()

        # Verify title of START-UP GUIDES page
        try:
            assert driver.title == "Guides - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11328").click()
        driver.find_element(By.LINK_TEXT, "NEWS & EVENTS").click()
        delay()

        # Verify title of NEWS & EVENTS page
        try:
            assert driver.title == "DAT News & Event Center - DAT"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11328").click()
        driver.find_element(By.LINK_TEXT, "VIDEOS").click()
        delay()

        # Verify title of VIDEOS page
        try:
            assert driver.title == "DAT Freight & Analytics - YouTube"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        delay()
        driver.find_element(By.ID, "menu-item-11328").click()
        driver.find_element(By.LINK_TEXT, "VIEW ALL RESOURCES").click()
        delay()

        # Verify title of VIEW ALL RESOURCES page
        try:
            assert driver.title == "Resource Library - DAT Freight & Analytics - Resource Center"
            print("The driver title is correct: ", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.back()
        print("Submenu of 'Resources' is correct")
    except AssertionError:
        print("Submenu of 'Resources' is wrong")
    delay()


def verify_contact_header(driver):  # Verify functionality of "Contact" menu in header
    driver.find_element(By.ID, "menu-item-12842").click()

    # Verify title of 'Contact' page
    try:
        assert driver.title == "Customer Support - DAT"
        print("The driver title is correct: ", driver.title)
    except AssertionError:
        print("Title is different. Current Title is:", driver.title)
    driver.back()
    delay()


def verify_search_header(driver):  # Verify functionality of "Search" menu in header
    driver.find_element(By.ID, "menu-item-12548").click()  # icon of search
    delay()
    driver.find_element(By.XPATH, "//span[@aria-hidden='true']").click()  # close window of search

    # Verify functionality of "Login" menu in header
    driver.find_element(By.ID, "menu-item-12886").click()


def verify_login_header(driver):  # Verify title of 'Login' page
    try:
        assert driver.title == "Customer Login | DAT Power | TruckersEdge | Express | RateView - DAT"
        print("The driver title is correct: ", driver.title)
    except AssertionError:
        print("Title is different. Current Title is:", driver.title)
    driver.back()
    delay()


def verify_signup_header(driver):  # Verify functionality of "Signup" menu in header
    driver.find_element(By.ID, "menu-item-14352").click()

    # Verify title of 'Signup' page
    try:
        assert driver.title == "Load Board - DAT"
        print("The driver title is correct: ", driver.title)
    except AssertionError:
        print("Title is different. Current Title is:", driver.title)
    driver.back()
    delay()
