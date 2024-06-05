import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from POM.pages.login_page import LoginPage
## import class name in the login page

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10) # how much time it has to wait before fails
    yield driver #yield the webdriver instance
    driver.quit() #close the webdriver instance


def test_logintest(driver):
    login_page = LoginPage(driver)  # create object to call login_page.py 's class(LoginPage) elements and actions
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(2)
    login_page.enter_username("test")
    login_page.enter_password("test")
    login_page.click_login()

    '''
    username_field=driver.find_element(By.ID, "uname")
    password_field=driver.find_element(By.ID, "pwd")
    submit_button=driver.find_element(By.XPATH, "//input[@value='Login']")
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    time.sleep(2)
    '''

    assert "Successful" in driver.page_source

