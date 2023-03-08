from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def Login(driver, user, password):
    user_input = driver.find_element(By.ID,"user-name")
    user_input.send_keys(user)
    user_input.send_keys(Keys.RETURN)
    
    
    pass_input = driver.find_element(By.ID, "password")
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.RETURN)

def clickButtonByName(driver, ButtonName):
    driver.find_element(By.NAME, ButtonName).click()