''' ### Webdriver methods/commands #########
Application specific =  get Commands -  title, curent_url, page_source
conditional == Is displayed(), is enabled(), is selected(). ( accessed visa webelement)
browser == Close(), QUIT() - (accessed via driver object)
          Close Closes active browser but process is still running. Quit kills process too.
navigational == Back(), forward(), refresh() - accessed via driver object)
wait
'''
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)
print("page source is",driver.page_source)



time.sleep(2)

##### FIND element and FIND Elements

driver.close()