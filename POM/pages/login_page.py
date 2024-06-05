from selenium.webdriver.common.by import By

class LoginPage:
    ### CONSTRUCTOR
    def __init__(self, driver):
        self.driver = driver
    ####Page Objects
        self.username_textbox = (By.ID, "uname")
        self.password_textbox = (By.ID, "pwd")
        self.login_button = (By.XPATH, "//input[@value='Login']")
    #####ACTIONS/METHODS on this page
    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        # Splat operator is *
    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
