from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL = (By.XPATH, "/html/body/div[3]/form/p[1]/input")
    PASSWORD = (By.XPATH, "/html/body/div[3]/form/p[2]/input")
    SUBMIT_BUTTON = (By.ID, "submit")


