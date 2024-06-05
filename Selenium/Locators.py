'''
LOCATORS:
Identify Elements- using ID, Name, Class name, TAG NAME, LINKedText,Partial LInked Text XPATH, CSS SELECTOR
CSS Selector - TAG and ID, TAG and CLASS, TAG and attribute, TAG Class and ATTRIBUTRE
XPATH - RELATIVE and ABsoulute
'''


import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com")
time.sleep(2)
driver.maximize_window()

#ID and NAME
#driver.find_element(By.ID, "small-searchterms").send_keys("Lenova")

#####    Linkedtext/Partial Link Text ( Cannot see name or ID, ---it has a and href)  #######
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()

## CLASS NAME (If we need to go with more than one element - Class name and Tag name needed)

#sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")

#links=driver.find_elements(By.TAG_NAME,"homeslider-container")
#print(len(links))

sliders=driver.find_elements(By.CLASS_NAME,"nivo-imageLink")
print("SLiders are: ",sliders)
print(len(sliders))

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

driver.quit()