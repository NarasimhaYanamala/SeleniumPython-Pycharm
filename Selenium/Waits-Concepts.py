'''
To handle Synchronization problems
#time.sleep ###
Adv: Single statement
Dis-adv: It waits even element is available, Performance is poor
If element is not available chance of exception
####IMPLICIT WAIT - Driver Level###
Adv:
Applicable for all below statements after stating- One statement handle all
It will wait until within the time mentioned but It will not wait for maximum timeout
Once element is available it quits waiting. So Performance increases
DIS-ADV: If Element is not available within mentioned time, it throws EXCEPTION
solution: use try catch exception method to proceed
####EXPLICIT WAIT - with Condiition - Element Level###
Adv:It works based on condition - We wont depend on time ( Just declare cut off time )
Execption handing is inbuilt
More effective
DisAdv: declare more plces
we

'''
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
#driver.implicitly_wait(10)
#driver.



''' IMPLICIT WAIT - Driver Level
Applicable for all below statements after stating- One statement handle all 
It will not wait for maximum timeout, Once element is available it quits waiting. So Performance increases
'''

''''
Explicit Wait - Decalaration and Utilization
'''
# Explicit wait decalaration

# why in explicit wait decaration, time is specified it womt depend on time.
# But there is a limit to wait for element as it should not wait unlimited. it is cutoff time.
# pole is like frequesncy - 2 sec mean it will do 5 times


driver.get("https://google.com")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH, "//*[text()='Accept all']").click()
time.sleep(1)
driver.find_element(By.NAME,"q").send_keys("Selenium")
driver.find_element(By.NAME,"q").submit()
#driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
mywait=WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                           ElementNotVisibleException,
                                                           ElementNotSelectableException,
                                                           Exception])

searchlink= mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))  ## Explicit wait utilization
searchlink.click()

driver.quit()