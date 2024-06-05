import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com")
time.sleep(2)
#Locator matching single web element
element=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
element.send_keys("Samsung")


# Locator matching multiple webelements
# Element1=driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(Element1.text)

#Element not available then throw No such element exception
# login_element=driver.find_element(By.LINK_TEXT, "Log in")
#print("Size is ",login_element.size)
# login_element.click()

# FIND ELEMENTS ( IT returns LIST Collection)
# elements=driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))
# print(elements[0].text)
# print(elements[0].send_keys("Apple MacBook Pro 13-inch"))

footerElements=driver.find_elements(By.XPATH, "//div[@class='footer']//a")
#print(footerElements.text)
print(footerElements)


print("Length is ", len(footerElements))
print("Text in first link is ", footerElements[1].text)
#
# for linkelement in footerElements:
#     print(linkelement.text)


#######  Text vs Get Attribute ############
#
# print(driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").text)
# print((driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").get_attribute('class')))


driver.quit()
