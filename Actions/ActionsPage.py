import time

from selenium.webdriver.support import expected_conditions as EC
from _pytest.config import Config
from selenium.webdriver.support.wait import WebDriverWait

from Locators.LocatorsThinker import CreateAccountLocators, SignInLocators


class Action_Page:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_create_account_url(self, url):
        self.driver.get(url)

    def click_signup_button(self,):
        click_sign_up = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CreateAccountLocators.SIGNUP_BUTTON))
        click_sign_up.click()
        time.sleep(Config.WAIT_TIME)

    def enter_firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CreateAccountLocators.FIRSTNAME))
        enter_firstname.send_keys(firstname)
        time.sleep(Config.WAIT_TIME)

    def enter_lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CreateAccountLocators.LASTNAME))
        enter_lastname.send_keys(lastname)
        time.sleep(Config.WAIT_TIME)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CreateAccountLocators.EMAIL))
        enter_email.send_keys(email)
        time.sleep(Config.WAIT_TIME)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CreateAccountLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(Config.WAIT_TIME)

    def click_submit(self, ):
        click_submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CreateAccountLocators.SUBMIT))
        click_submit.click()
        time.sleep(Config.WAIT_TIME)

class sign_in_Page:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(SignInLocators.EMAIL))
        enter_email.send_keys(email)
        time.sleep(Config.WAIT_TIME)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(SignInLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(Config.WAIT_TIME)

    def click_submit(self, ):
        click_submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(SignInLocators.SUBMIT))
        click_submit.click()
        time.sleep(Config.WAIT_TIME)

class InvalidLogin_Page:
    def __init__(self, driver):
        self.driver = driver

    def enter_valid_email(self, valid_email):
        enter_valid_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(InvalidLogInLocators.VALID_EMAIL))
        enter_valid_email.send_keys(valid_email)
        time.sleep(Config.WAIT_TIME)

    def enter_password_nul(self, password_nul):
        enter_password_nul = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(InvalidLogInLocators.PASSWORD_NUL))
        enter_password_nul.send_keys(password_nul)
        time.sleep(Config.WAIT_TIME)

    def click_submit_button(self, ):
        click_submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(InvalidLogInLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(Config.WAIT_TIME)

class AddNewContact_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact(self, ):
        click_add_new_contact = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(Config.WAIT_TIME)

    def enter_firstname1(self, firstname1):
        enter_firstname1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.FIRSTNAME1))
        enter_firstname1.send_keys(firstname1)
        time.sleep(Config.WAIT_TIME)

    def enter_lastname1(self, lastname1):
        enter_lastname1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.LASTNAME1))
        enter_lastname1.send_keys(lastname1)
        time.sleep(Config.WAIT_TIME)

    def enter_date_birth1(self, date_birth1):
        enter_date_birth1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.DATE_BIRTH1))
        enter_date_birth1.send_keys(date_birth1)
        time.sleep(Config.WAIT_TIME)

    def enter_email1(self, email1):
        enter_emai1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.EMAIL1))
        enter_emai1.send_keys(email1)
        time.sleep(Config.WAIT_TIME)

    def enter_phone1(self, phone1):
        enter_phone1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.PHONE1))
        enter_phone1.send_keys(phone1)
        time.sleep(Config.WAIT_TIME)

    def enter_street_address(self, street_address):
        enter_street_address = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.STREET_ADDRESS))
        enter_street_address.send_keys(street_address)
        time.sleep(Config.WAIT_TIME)

    def enter_city(self, city):
        enter_city = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.CITY))
        enter_city.send_keys(city)
        time.sleep(Config.WAIT_TIME)

    def enter_state_province(self, state_province):
        enter_state_province = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.STATE_PROVINCE))
        enter_state_province.send_keys(state_province)
        time.sleep(Config.WAIT_TIME)

    def enter_postal_code(self, postal_code):
        enter_postal_code = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.POSTAL_CODE))
        enter_postal_code.send_keys(postal_code)
        time.sleep(Config.WAIT_TIME)

    def enter_country(self, country):
        enter_country = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.COUNTRY))
        enter_country.send_keys(country)
        time.sleep(Config.WAIT_TIME)

    def click_submit1(self, submit1):
        enter_submit1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.SUBMIT1))
        enter_submit1.send_keys(submit1)
        time.sleep(Config.WAIT_TIME)
