from selenium import webdriver

def headless_chrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.headless=True
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title, driver.current_url)
print("Window handles: ", driver.window_handles)

driver.quit()

