#Variables 
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
    time.sleep(1)

def Login(driver):
    elem = driver.find_element(By.ID,"user-name")
    elem.send_keys("standard_user")
    elem.send_keys(Keys.RETURN)
    

    elem = driver.find_element(By.ID, "password")
    elem.send_keys("secret_sauce")
    elem.send_keys(Keys.RETURN)
    


    driver.find_element(By.ID, "login-button").click()
    assert "Products" in driver.page_source 

def boton_D(driver):
    botonDesplegable = driver.find_element(By.CLASS_NAME, "product_sort_container").click()
 

def FirstElement(driver):
    OrdenPrice = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[3]").click()
    SelectionFirstItem = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div").click()
    addtocart = driver.find_element(By.NAME,"add-to-cart-sauce-labs-onesie").click()
    BacktoProducts = driver.find_element(By.ID,"back-to-products").click()

def BuylightBike(driver):
    Bikelight = driver.find_element(By.CLASS_NAME, "inventory_item_desc")
    assert "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included." in driver.page_source
    addtocartBikelight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()


def OrdenProducts(driver):
    botonDesplegable = driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    OrdenProducts = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[2]").click()

def RemoveandAdd(driver):
    RemoveArt = driver.find_element(By.ID,"remove-sauce-labs-onesie").click()
    TshirtRed = driver.find_element(By.LINK_TEXT, "Test.allTheThings() T-Shirt (Red)").click()
    Addproduct = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()



def firstCart(driver):
    Cart = driver.find_element(By.ID, "shopping_cart_container").click()
    assert "Your Cart" in driver.page_source
    RemoveofCart = driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()


def BackandOrden(driver):
    BacktoProducts = driver.find_element(By.ID, "continue-shopping").click()
    botonDesplegable = driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    PriceHightoLow = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[4]").click()

def AddandCart(driver):
    AddJacket = driver.find_element(By.NAME, "add-to-cart-sauce-labs-fleece-jacket").click()
    Cart = driver.find_element(By.LINK_TEXT, "2").click()


def checkout(driver):
    checkout =driver.find_element(By.ID, "checkout").click()
    assert "Checkout: Your Information" in driver.page_source

def Information(driver):
    informationFirstName = driver.find_element(By.ID, "first-name")
    informationFirstName.send_keys("jeronimo")
    informationLastName = driver.find_element(By.ID, "last-name")
    informationLastName.send_keys("tomas")
    informationCodigoPostal = driver.find_element(By.ID, "postal-code")
    informationCodigoPostal.send_keys("5519")
    time.sleep(3)


def Finish(driver):
    BtnContinue = driver.find_element(By.NAME, "continue").click()
    time.sleep(2)
    assert "Checkout: Overview" in driver.page_source
    finish = driver.find_element(By.NAME, "finish").click()
    assert "Checkout: Complete!" in driver.page_source


def Back(driver):
    BackHome = driver.find_element(By.NAME, "back-to-products").click()


def LinkgoTw(driver):
    GOtwitter = driver.find_element(By.LINK_TEXT, "Twitter").click()


#test1 
driver= setCRoptions()
OpenBrowser(driver)
Login(driver)
boton_D(driver)
FirstElement(driver)
BuylightBike(driver)
OrdenProducts(driver)
RemoveandAdd(driver)
firstCart(driver)
BackandOrden(driver)
AddandCart(driver)
checkout(driver)
Information(driver)
Finish(driver)
Back(driver)
LinkgoTw(driver)

driver.quit()






