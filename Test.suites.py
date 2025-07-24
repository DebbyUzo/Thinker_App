import pytest
from _pytest.config import Config
from selenium.webdriver.chrome import webdriver

from Actions.ActionsPage import Action_Page


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.ChromiumDriver()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope = "session")
def signup(driver_setup):
    driver = driver_setup
    sign_up = Action_Page(driver)
    sign_up.navigate_to_signup_url(Config.BASE_URL)
    return sign_up

def test_sign_up_button_on_automation_add_contact(signup):
    signup.click_signup_button()
    signup.enter_firstname("Dabo")
    signup.enter_lastname("Ego")
    signup.enter_email("otoline@yahoo.com")
    signup.enter_password("Ego123@")
    signup.click_submit()

def test_login_page_on_automation_contact_list_website(login):
    login.enter_email("otolinedebby@yahoo.com")
    login.enter_password("Ego123@")
    login.click_login_submit()

def test_invalid_login_page(login):
    login.enter_email("otolinedebby@yahoo.com")
    login.enter_password("nul")
    login.click_login_submit()

def test_add_new_contact_page(login):
    add_new_contact  = AddNewContact_Page(login)
    add_new_contact.click_add_new_contact()
    add_new_contact.enter_firstname1("Fav")
    add_new_contact.enter_lastname1("James")
    add_new_contact.enter_date_birth1("1993/05/25")
    add_new_contact.enter_email1("favjames@yahoo.com")
    add_new_contact.enter_phone1("0902345678")
    add_new_contact.enter_street_address("Ilori street")
    add_new_contact.enter_city("Okota")
    add_new_contact.enter_state_province("Lagos")
    add_new_contact.enter_postal_code("12345")
    add_new_contact.enter_country("Nigeria")
    add_new_contact.click_submit1()
