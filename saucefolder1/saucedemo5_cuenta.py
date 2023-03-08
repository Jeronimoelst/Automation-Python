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

def VerifyText (driver, Text):
    assert Text in driver.page_source

def Cart (driver, Cart):
    driver.find_element(By.ID, Cart).click()

def Information(driver, firstName, lastName, cp):
    informationFirstName = driver.find_element(By.ID, "first-name")
    informationFirstName.send_keys(firstName)
    informationLastName = driver.find_element(By.ID, "last-name")
    informationLastName.send_keys(lastName)
    informationCodigoPostal = driver.find_element(By.ID, "postal-code")
    informationCodigoPostal.send_keys(cp)
    

def Precio1(driver, P1):
    precio1 = driver.find_element(By.CLASS_NAME, P1).text
    return precio1

def Precio2(driver, P2):
    precio2 = driver.find_element(By.CLASS_NAME, P2).text
    return precio2

def ItemTotal(driver, I):
    IT = driver.find_element(By.CLASS_NAME, I).text
    return IT

def suma(precio1, precio2, IT):
    sum = precio1 + precio2
    sum = IT 
    return IT




#test1
driver = setCRoptions()
OpenBrowser(driver)
Login(driver, "performance_glitch_user" , "secret_sauce")
clickButtonByName(driver, "login-button")
VerifyText (driver, "Products")
clickButtonByName (driver, "add-to-cart-sauce-labs-backpack")
clickButtonByName (driver, "add-to-cart-sauce-labs-bike-light")
clickButtonByName (driver, "add-to-cart-sauce-labs-bolt-t-shirt")
clickButtonByName (driver, "add-to-cart-sauce-labs-fleece-jacket")
Cart(driver, "shopping_cart_container")
VerifyText(driver, "Your Cart")
clickButtonByName(driver, "remove-sauce-labs-backpack")
clickButtonByName(driver, "remove-sauce-labs-bike-light")
clickButtonByName(driver, "checkout")
Information(driver, "juan", "agustin", 3455)
clickButtonByName(driver, "continue")
VerifyText(driver, "Checkout: Overview")
Precio1(driver, "inventory_item_price")
Precio2(driver, "inventory_item_price")
ItemTotal(driver, "summary_subtotal_label")
VerifyText(driver, "65.98")
clickButtonByName(driver, "finish")
VerifyText(driver, "Checkout: Complete!") 
clickButtonByName(driver, "back-to-products")
VerifyText(driver, "Products") 

driver.quit()


