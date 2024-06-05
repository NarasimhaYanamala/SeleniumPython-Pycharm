import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://trytestingthis.netlify.app/index.html")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.ID,"lname").send_keys("Rao")
driver.find_element(By.ID,"fname").send_keys("NR")
driver.find_element(By.XPATH,"//input[@value='login']")

#/html/body/div[3]/div[1]/fieldset/form/div/input[3]
#//input[@value='Login']
#input[value='Login']