import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10) # how much time it has to wait before fails
    yield driver #yield the webdriver instance
    driver.quit() #close the webdriver instance

@pytest.mark.parametrize("username, password",[
    ("test", "test"),
    ("user2", "pass2"),
    ("user3", "pass3"),
])

def test_logintest(driver,username,password):
    driver.get("https://trytestingthis.netlify.app/")
    time.sleep(2)
    username_field=driver.find_element(By.ID, "uname")
    password_field=driver.find_element(By.ID, "pwd")
    submit_button=driver.find_element(By.XPATH, "//input[@value='Login']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    time.sleep(2)

    assert "Successful" in driver.page_source