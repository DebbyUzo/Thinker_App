from selenium.webdriver.common.by import By

class CreateAccountLocators:
    SIGNUP_BUTTON = (By.ID, "signup")
    FIRSTNAME = (By.ID, "firstName")
    LASTNAME = (By.ID, "lastName")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")

class SignInLocators:
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")

class IncorrectCredentials:
    VALID_EMAIL = (By.ID, "email")
    PASSWORD_NUL = (By.ID, "")
    SUBMIT_BUTTON = (By.ID, "submit")

class AddContactList:
    ADD_NEW_CONTACT = (By.ID, "add-contact")
    FIRSTNAME1 = (By.ID, "firstName")
    LASTNAME1 = (By.ID, "lastName")
    DATE_BIRTH1 = (By.ID, "birthdate")
    EMAIL1 = (By.ID, "email")
    PHONE1 = (By.ID, "phone")
    STREET_ADDRESS = (By.ID, "street1")
    CITY = (By.ID, "city")
    STATE_PROVINCE = (By.ID, "stateProvince")
    POSTAL_CODE = (By.ID, "postalCode")
    COUNTRY = (By.ID, "country")
    SUBMIT1 = (By.ID, "submit")