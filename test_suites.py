import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Actions.ActionsPage import Action_Page, AddNewContact_Page

from Actions.ActionsPage import AddNewFirstContact_Page
from Config.Configuration import Config

# Fixture to launch browser
@pytest.fixture(scope="session")
def driver_setup():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

# Fixture to perform login
@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = Action_Page(driver)
    login_page.login_url(Config.BASEURL)
    return login_page

# Test: Successful login
def test_login_with_valid_credentials(login):
    login.enter_email("otolinedebby@yahoo.com")
    login.enter_password("Ego123@")
    login.click_submit()

# Test: Add New Contact
def test_add_new_contact_successfully(login):
    add_new_contact = AddNewContact_Page(login)
    add_new_contact.click_add_new_contact()

# Test: Add New Contact
def test_add_new_contact_successfully(login):
    add_contact = AddContact_Page(login)
    add_contact.enter_firstname(Config.FIRSTNAME)
    add_contact.enter_lastname(Config.LASTNAME)
    add_contact.enter_date_birth(Config.DATE_BIRTH)
    add_contact.enter_email1(Config.EMAIL)
    add_contact.enter_phone(Config.PHONE)
    add_contact.enter_street_address(Config.STREET_ADDRESS)
    add_contact.enter_city(Config.CITY)
    add_contact.enter_state_province(Config.STATE_PROVINCE)
    add_contact.enter_postal_code(Config.POSTAL_CODE)
    add_contact.enter_country(Config.COUNTRY)
    add_contact.click_submit1()

# Test: Add 2nd New Contact
def test_add_new_contact_successfully(login):
    add_newcontact = AddNewContact_Page(login)
    add_newcontact.click_add_new_contact()
    add_Newcontact.enter_firstname(Config.FIRSTNAME)
    add_newcontact.enter_lastname(Config.LASTNAME)
    add_newcontact.enter_date_birth(Config.DATE_BIRTH)
    add_newcontact.enter_email(Config.EMAIL)
    add_newcontact.enter_phone(Config.PHONE)
    add_newcontact.enter_street_address(Config.STREET_ADDRESS)
    add_newcontact.enter_city(Config.CITY)
    add_newcontact.enter_state_province(Config.STATE_PROVINCE)
    add_newcontact.enter_postal_code(Config.POSTAL_CODE)
    add_newcontact.enter_country(Config.COUNTRY)
    add_newcontact.click_submit()

# Test: Add 3rd New Contact
def test_add_new_first_contact_successfully(login):
    add_NewFirstContact = AddNewFirstContact_Page(login)
    add_NewFirstContact.click_add_new_contact()
    add_NewFirstContact.enter_firstname()

