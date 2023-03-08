from CRoptions_page import *
from openBrowser_page import *
from Login_page import *
from Cart_page import *
from Information_page import *
from helper import *

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
clickButtonByName(driver, "finish")
VerifyText(driver, "Checkout: Complete!") 
clickButtonByName(driver, "back-to-products")
VerifyText(driver, "Products") 

driver.quit()
