## How to capture screenshot of an application
import time
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/")

#driver.save_screenshot("C:\\Users\\ynrbt\\OneDrive - kwamenkrumahacademy.org\\Automation\\homepage.png")
driver.save_screenshot(os.getcwd()+"\\homepage.png")
driver.quit()