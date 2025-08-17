
from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL = (By.XPATH, "/html/body/div[3]/form/p[1]/input")
    PASSWORD = (By.XPATH, "/html/body/div[3]/form/p[2]/input")
    SUBMIT_BUTTON = (By.ID, "submit")

class AddContactLocators:
    ADD_NEW_CONTACT = (By.ID, "add-contact")
    FIRSTNAME = (By.ID, "firstName")
    LASTNAME = (By.XPATH, "/html/body/div/form/p[1]/input[2]")
    DATE_BIRTH = (By.ID, "birthdate")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    STREET_ADDRESS = (By.ID, "street1")
    CITY = (By.ID, "city")
    STATE_PROVINCE = (By.ID, "stateProvince")
    POSTAL_CODE = (By.ID, "postalCode")
    COUNTRY = (By.ID, "country")
    SUBMIT = (By.ID, "submit")

class AddNewContactLocators:
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
