## How to capture screenshot of an application
import time
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.implicitly_wait(10)


# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# RegLink_tab=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(RegLink_tab)

###New Tab in Selenium 4
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://orangehrm.com/")

###New window in Selenium 4
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://orangehrm.com/")
