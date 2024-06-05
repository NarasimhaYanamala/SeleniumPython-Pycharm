import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click() #Selecting UK

CountriesList=driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(CountriesList))

for country in CountriesList:
    if country.text=='India':
        country.click()
        break

driver.quit()