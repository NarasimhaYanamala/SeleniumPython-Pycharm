import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)
username=driver.find_element(By.NAME,"username")
username.send_keys("Admin")
password=driver.find_element(By.NAME,"password")
password.send_keys("admin123")
Loginbutton=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
Loginbutton.send_keys(Keys.RETURN)

Actual_Title=driver.title
ExpectedTitle="OrangeHRM"
print(driver.window_handles)
if Actual_Title == ExpectedTitle:
    print("Login is successful")
else:
    print("Login is not successful")

driver.close()
driver.quit()