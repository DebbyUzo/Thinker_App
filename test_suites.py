import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Actions.ActionsPage import Login_Page, AddContact_Page, AddNewContact_Page
from Config.Configuration import Config

# Fixture to launch browser
@pytest.fixture(scope="session")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

# Fixture to perform login
@pytest.fixture(scope="session")
def login(driver_setup):
    login_page = Login_Page(driver_setup)
    login_page.navigate_to_login_url(Config.BASE_URL)
    return driver_setup  # return driver for next tests

# Test: Successful login
def test_login_with_valid_credentials(login):
    login.enter_email(Config.EMAIL)
    login.enter_password(Config.PASSWORD)
    login.click_submit()

# Test: Add New Contact
def test_add_new_contact_successfully(login):
    add_contact = AddContact_Page(login)
    add_contact.click_add_new_contact()
    add_contact.enter_firstname(Config.FIRSTNAME)
    add_contact.enter_lastname(Config.LASTNAME)
    add_contact.enter_date_birth(Config.DATE_BIRTH)
    add_contact.enter_email1("otolinedebby@yahoo.com")
    add_contact.enter_phone(Config.PHONE)
    add_contact.enter_street_address(Config.STREET_ADDRESS)
    add_contact.enter_city(Config.CITY)
    add_contact.enter_state_province(Config.STATE_PROVINCE)
    add_contact.enter_postal_code(Config.POSTAL_CODE)
    add_contact.enter_country(Config.COUNTRY)
    add_contact.click_submit1()

# Test: Add 2nd New Contact
def test_add_new_contact_successfully(login):
        add_Newcontact = AddNewContact_Page(login)
        add_Newcontact.click_add_new_contact()
        add_Newcontact.enter_firstname(Config.FIRSTNAME)
        add_Newcontact.enter_lastname(Config.LASTNAME)
        add_Newcontact.enter_date_birth(Config.DATE_BIRTH)
        add_Newcontact.enter_email(Config.EMAIL)
        add_Newcontact.enter_phone(Config.PHONE)
        add_Newcontact.enter_street_address(Config.STREET_ADDRESS)
        add_Newcontact.enter_city(Config.CITY)
        add_Newcontact.enter_state_province(Config.STATE_PROVINCE)
        add_Newcontact.enter_postal_code(Config.POSTAL_CODE)
        add_Newcontact.enter_country(Config.COUNTRY)
        add_Newcontact.click_submit()


