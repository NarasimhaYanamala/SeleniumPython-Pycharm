import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#Capture Cookies from Browser
''''
Every Cookie :  name="xyz"
                Value=1234
                Expiry date=date

***like a key value pair, Dictionary collection set - Store in Dict object
'''

cookies=driver.get_cookies()
print("Size of cookies: ", len(cookies)) #5

for cookie in cookies:
    #print(cookie) ### Dictionary objects
    print(cookie.get('name'), cookie.get('value'))  ## Only Extracting name and Value from Dict collection


### ADD A NEW COOKIE
#driver.add_cookie()  ### Pass only in DICT format (Key pair) as it allows in that format only

# driver.add_cookie({"name": "MyCookie", "value":"123456"})
# ##Size of cookies after adding onemore time
# cookies=driver.get_cookies()
# print("Size of cookies after adding new one: ", len(cookies)) #5


# driver.delete_cookie("MyCookie")
#driver.delete_all_cookies()


driver.quit()