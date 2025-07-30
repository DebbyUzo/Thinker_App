import pytest
from selenium import webdriver

from Actions.ActionsPage import Login_Page
from Config.Configuration import Config

@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

# Fixture to set up and tear down the browser
@pytest.fixture(scope = "session")
def log_in(driver_setup):
    driver = driver_setup
    login = Login_Page(driver)
    login.navigate_to_login_url(Config.BASE_URL)
    return login

# Test for successful sign in
def test_login_with_valid_credentials(login):
    login = Login_Page(login)
    login.enter_email("otolinedebby@yahoo.com")
    login.enter_password("dapo123")
    login.click_submit()
