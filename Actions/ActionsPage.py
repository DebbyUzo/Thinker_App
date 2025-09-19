import time

from selenium.webdriver.support import expected_conditions as EC
from _pytest.config import Config
from selenium.webdriver.support.wait import WebDriverWait

from Locators.LocatorsThinker import LoginLocators, AddContactLocators, AddNewContactLocators, \
    AddNewFirstContactLocators, AddANewContactLocators

class Action_Page:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)
        time.sleep(10)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.EMAIL))
        enter_email.send_keys(email)
        time.sleep(10)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(10)

    def click_submit(self, ):
        click_submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        click_submit.click()
        time.sleep(10)

class AddANewContact_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_add_a_new_contact(self, ):
        click_add_a_new_contact = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddANewContactLocators.ADD_A_NEW_CONTACT))
        click_add_a_new_contact.click()
        time.sleep(10)

class AddContact_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact(self, ):
        click_add_new_contact = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(10)

    def enter_firstname(self, firstname1):
        enter_firstname1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.FIRSTNAME1))
        enter_firstname1.send_keys(firstname1)
        time.sleep(10)

    def enter_lastname(self, lastname1):
        enter_lastname1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.LASTNAME1))
        enter_lastname1.send_keys(lastname1)
        time.sleep(10)

    def enter_date_birth(self, date_birth1):
        enter_date_birth1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.DATE_BIRTH1))
        enter_date_birth1.send_keys(date_birth1)
        time.sleep(10)

    def enter_email1(self, email1):
        enter_emai1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.EMAIL1))
        enter_emai1.send_keys(email1)
        time.sleep(10)

    def enter_phone(self, phone1):
        enter_phone1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.PHONE1))
        enter_phone1.send_keys(phone1)
        time.sleep(10)

    def enter_street_address(self, street_address):
        enter_street_address = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.STREET_ADDRESS))
        enter_street_address.send_keys(street_address)
        time.sleep(10)

    def enter_city(self, city):
        enter_city = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.CITY))
        enter_city.send_keys(city)
        time.sleep(10)

    def enter_state_province(self, state_province):
        enter_state_province = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.STATE_PROVINCE))
        enter_state_province.send_keys(state_province)
        time.sleep(10)

    def enter_postal_code(self, postal_code):
        enter_postal_code = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.POSTAL_CODE))
        enter_postal_code.send_keys(postal_code)
        time.sleep(10)

    def enter_country(self, country):
        enter_country = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.COUNTRY))
        enter_country.send_keys(country)
        time.sleep(10)

    def click_submit1(self, submit1):
        enter_submit1 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddContactLocators.SUBMIT1))
        enter_submit1.send_keys(submit1)
        time.sleep(10)

class AddNewContact_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact(self, ):
        click_add_new_contact = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.ADD_NEW_CONTACT))
        click_add_new_contact.click()
        time.sleep(10)

    def enter_firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.FIRSTNAME1))
        enter_firstname.send_keys(firstname)
        time.sleep(10)

    def enter_lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.LASTNAME1))
        enter_lastname.send_keys(lastname)
        time.sleep(10)

    def enter_date_birth(self, date_birth):
        enter_date_birth = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.DATE_BIRTH1 ))
        enter_date_birth.send_keys(date_birth)
        time.sleep(10)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.EMAIL1))
        enter_email.send_keys(email)
        time.sleep(10)

    def enter_phone(self, phone):
        enter_phone = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.PHONE1))
        enter_phone.send_keys(phone)
        time.sleep(10)

    def enter_street_address(self, street_address):
        enter_street_address = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.STREET_ADDRESS))
        enter_street_address.send_keys(street_address)
        time.sleep(10)

    def enter_city(self, city):
        enter_city = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.CITY))
        enter_city.send_keys(city)
        time.sleep(10)

    def enter_state_province(self, state_province):
        enter_state_province = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.STATE_PROVINCE))
        enter_state_province.send_keys(state_province)
        time.sleep(10)

    def enter_postal_code(self, postal_code):
        enter_postal_code = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.POSTAL_CODE))
        enter_postal_code.send_keys(postal_code)
        time.sleep(10)

    def enter_country(self, country):
        enter_country = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.COUNTRY))
        enter_country.send_keys(country)
        time.sleep(10)

    def click_submit(self, submit):
        enter_submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewContactLocators.SUBMIT1))
        enter_submit.send_keys(submit)
        time.sleep(10)

class AddNewFirstContact_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact(self, ):
        click_add_new_contact = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.ADD_NEW_FIRST_CONTACT))
        click_add_new_contact.click()
        time.sleep(10)

    def enter_firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.FIRSTNAME))
        enter_firstname.send_keys(firstname)
        time.sleep(10)

    def enter_lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.LASTNAME))
        enter_lastname.send_keys(lastname)
        time.sleep(10)

    def enter_date_birth(self, date_birth):
        enter_date_birth = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.DATE_BIRTH))
        enter_date_birth.send_keys(date_birth)
        time.sleep(10)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.EMAIL))
        enter_email.send_keys(email)
        time.sleep(10)

    def enter_phone(self, phone):
        enter_phone = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.PHONE))
        enter_phone.send_keys(phone)
        time.sleep(10)

    def enter_street_address(self, street_address):
        enter_street_address = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.STREET_ADDRESS))
        enter_street_address.send_keys(street_address)
        time.sleep(10)

    def enter_city(self, city):
        enter_city = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.CITY))
        enter_city.send_keys(city)
        time.sleep(10)

    def enter_state_province(self, state_province):
        enter_state_province = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.STATE_PROVINCE))
        enter_state_province.send_keys(state_province)
        time.sleep(10)

    def enter_postal_code(self, postal_code):
        enter_postal_code = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.POSTAL_CODE))
        enter_postal_code.send_keys(postal_code)
        time.sleep(10)

    def enter_country(self, country):
        enter_country = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.COUNTRY))
        enter_country.send_keys(country)
        time.sleep(10)

    def click_submit(self, submit):
        enter_submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddNewFirstContactLocators.SUBMIT))
        enter_submit.send_keys(submit)
        time.sleep(10)