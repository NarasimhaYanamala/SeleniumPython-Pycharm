import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://admin-demo.nopcommerce.com/login")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys('admin@yourstore.com')
driver.find_element(By.XPATH, "//input[@id='Password']").clear()
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('admin')
time.sleep(2)
#print(driver.find_element(By.XPATH, "//input[@name='RememberMe']").is_enabled())
#driver.find_element(By.XPATH, "//input[@name='RememberMe']").clear()
#driver.find_element((By.XPATH, "//button[@type='submit']")
#driver.find_element(By.CSS_SELECTOR, "")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


assert (driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/h1").is_displayed()) == True
dashboardVisibility=driver.find_element(By.CSS_SELECTOR, "div[class='content-header'] h1").is_displayed()
print(dashboardVisibility)
textDashboard=driver.find_element(By.XPATH, "//h1[normalize-space()='Dashboard']").text
print(textDashboard)


driver.quit()