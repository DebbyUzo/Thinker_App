import time

import pytest
from selenium import webdriver

from Actions.ActionsPage import Login_Page
from Config.Configuration import Config

# Fixture to launch browser
@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

# Fixture to prepare the login page
@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login = Login_Page(driver_setup)
    login.navigate_to_login_url(Config.BASE_URL)
    return login

# Test for successful login
def test_login_with_valid_credentials(login):
    login.enter_email(Config.EMAIL)
    login.enter_password(Config.PASSWORD)
    login.click_submit()
