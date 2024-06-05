''''
Create Google Search test in Selenium
Use Pytest Fixtures for Setup and Tear down
Use Parameterization with Pytest
'''
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10) # how much time it has to wait before fails
    #yield the webdriver instance
    yield driver
    #close the webdriver instance
    driver.quit()

def test_google_search(driver):
    driver.get("https://google.com")
    time.sleep(2)
    #print("Text is ", driver.find_elements(By.XPATH, "//div[@class='QS5gu sy4vM']").__getitem__(1).text)
    # print(findelements)
    driver.find_element(By.XPATH, "//*[text()='Accept all']").click()
    googleSearchBox=driver.find_element(By.ID, "APjFqb")
    googleSearchBox.send_keys("Automation")
    googleSearchBox.send_keys(Keys.RETURN)
    time.sleep(2)
    print("Test Complete")





