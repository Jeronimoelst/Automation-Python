#refactorizacion
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

def setCRoptions():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sanbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("page load strategy")
    options.add_argument("--disable-web-security")
    options.add_argument("pageLoadStrategy")
    driver = webdriver.Chrome(options=options)
    return driver
    
def OpenBrowser(driver):
    driver.get('https://www.saucedemo.com/')
    

def Login(driver, user, password):
    elem = driver.find_element(By.ID,"user-name")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    

    elem = driver.find_element(By.ID, "password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

def clickButtonByName(driver, ButtonName):
    driver.find_element(By.NAME, ButtonName).click()

def BtnD(driver, BD):
    driver.find_element(By.XPATH, BD).click()

def btnlink(driver, link):
    driver.find_element(By.LINK_TEXT,link).click()

def Cart(driver, C):
    driver.find_element(By.XPATH,C).click()

def Information(driver, firstName, lastName, cp):
    informationFirstName = driver.find_element(By.ID, "first-name")
    informationFirstName.send_keys(firstName)
    informationLastName = driver.find_element(By.ID, "last-name")
    informationLastName.send_keys(lastName)
    informationCodigoPostal = driver.find_element(By.ID, "postal-code")
    informationCodigoPostal.send_keys(cp)


def VerifyEntry(driver, expctedText):
    assert expctedText in driver.page_source 


#test1
driver = setCRoptions()
OpenBrowser(driver)
Login(driver, "performance_glitch_user" , "secret_sauce")
clickButtonByName(driver, "login-button")
VerifyEntry(driver, "Products")
clickButtonByName(driver, "add-to-cart-sauce-labs-backpack")
BtnD(driver, "/html/body/div/div/div/div[1]/div[2]/div[2]/span/select")
BtnD(driver, "/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[2]")
btnlink(driver, "Sauce Labs Onesie")
clickButtonByName(driver, "add-to-cart-sauce-labs-onesie")
Cart(driver, "/html/body/div/div/div/div[1]/div[1]/div[3]")
clickButtonByName(driver, "checkout")
Information(driver, "jeronimo", "tomas", 5519)
clickButtonByName(driver, "continue")
clickButtonByName(driver, "finish")
VerifyEntry(driver, "Checkout: Complete!")
clickButtonByName(driver, "back-to-products")
driver.quit()



