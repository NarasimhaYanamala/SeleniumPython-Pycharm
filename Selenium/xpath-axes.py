import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.find_element(By.XPATH,"//p[text()='Consent']").click()
driver.maximize_window()
time.sleep(2)

#Self
selfText=driver.find_element(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/self::a").text
print(selfText)  #Computer Age Mgt

#Parent
parentText=driver.find_element(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/parent::td").text
print(parentText) #Computer Age Mgt


#Child
childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/ancestor::tr/child::td")
print(childs)

#ancestor
ancestorText=driver.find_element(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/ancestor::tr").text
print(ancestorText)

#descendant ( Above of the self nodes are descendant nodes, below are following nodes)
descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/ancestor::tr/descendant::*")
print("no of descendant nodes",descendants)
#following
following=driver.find_elements(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/ancestor::tr/following::*")
print("no of following nodes",len(following))

##following-siblings
followingSiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/ancestor::tr/following-sibling::*")
print("no of following siblings",len(followingSiblings))

#preceding
preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/ancestor::tr/preceding::*")
print("no of following nodes",len(preceding))

#preceding-Siblings
precedingSibling=driver.find_elements(By.XPATH,"//a[contains(text(),'Computer Age Mgt')]/ancestor::tr/preceding-sibling::*")
print("no of following nodes",len(precedingSibling))

driver.close()