from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginPageClass:

    pageUrl= "https://www.saucedemo.com/"

    def __init__(self,driver):
            self.pageUrl = "https://www.saucedemo.com/"
             #add implicit waits
            self.user_input = driver.find_element(By.ID,"user-name")
            self.pass_input = driver.find_element(By.ID, "password")


    def Login(self, user, password):
        self.user_input.send_keys(user)
        self.user_input.send_keys(Keys.RETURN)
        self.pass_input.send_keys(password)
        self.pass_input.send_keys(Keys.RETURN)
