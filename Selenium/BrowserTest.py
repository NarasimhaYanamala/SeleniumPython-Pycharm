import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10)
username=driver.find_element(By.NAME,"username")
username.send_keys("Admin")
password=driver.find_element(By.NAME,"password")
password.send_keys("admin123")
Loginbutton=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
#Loginbutton.click()
Loginbutton.send_keys(Keys.RETURN)





