import time

from selenium.webdriver.support import expected_conditions as EC
from _pytest.config import Config
from selenium.webdriver.support.wait import WebDriverWait

from Locators.LocatorsThinker import LoginLocators

class Login_Page:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.EMAIL))
        enter_email.send_keys(email)
        time.sleep(Config.WAIT_TIME)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(Config.WAIT_TIME)

    def click_submit(self, ):
        click_submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        click_submit.click()
        time.sleep(Config.WAIT_TIME)

