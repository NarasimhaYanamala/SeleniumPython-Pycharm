'''
EXCEL UTILs needed to do Data drivern test approach (BEST one)
pip install excel-util
#####  or   ####
Selenium - Wont support reading EXCEL sheet. we need 3rd party tools
openpyxl ( module to be isntalled - (.xlsx))
pip install openpyxl
'''
#### FIXED Depeosit Calculator
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Selenium.DataDrivenTesting import XLUtils  ##( Imported XL utils module here to use)
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.thecalculatorsite.com/finance/calculators/simple-interest-calculator.php")
driver.maximize_window()

file="C:\\Users\\ynrbt\\OneDrive - kwamenkrumahacademy.org\\Automation\\Calcdata.xlsx"
rows=XLUtils.getRowsCount(file,"Sheet1")
for r in range(2,rows+1):
    Starting_balance=XLUtils.readData(file,"Sheet1",r,1)  ##20000
    roi = XLUtils.readData(file, "Sheet1", r, 2)
    per1= XLUtils.readData(file, "Sheet1", r, 3)
    per2= XLUtils.readData(file, "Sheet1", r, 4)
    Freq = XLUtils.readData(file, "Sheet1", r, 5)
    exp_maturity = XLUtils.readData(file, "Sheet1", r, 6)
#passing data to the application
driver.find_element(By.XPATH,"//label[text()='₹']").click()
driver.find_element(By.XPATH,"//input[@name='amount']").send_keys(Starting_balance)
driver.find_element(By.XPATH,"//input[@id='percent']").send_keys(roi)
PeriodDrop=Select(driver.find_element(By.XPATH, "//select[@name='percentPeriod']"))
PeriodDrop.select_by_visible_text(per2)

ActualResult=driver.find_element(By.XPATH, "//div[@class='one']//span[1]").text

#Validation
if float(exp_maturity)==float(ActualResult):
    print("Test Passed")
    XLUtils.WriteData(file, "Sheet1", r, 8, "Passed")
    XLUtils.fillGreenColor(file, "Sheet1", r, 8)
else:
    print("Test Failed")
    XLUtils.WriteData(file, "Sheet1", r, 8, "Failed")
    XLUtils.fillRedColor(file, "Sheet1", r, 8)



driver.quit()





