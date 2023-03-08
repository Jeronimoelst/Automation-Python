from selenium.webdriver.common.by import By


class CartClass:

     def __init__(self, driver):
        self.pageURL = "https://www.saucedemo.com/cart.html"
         #add implicit waits
        self.Cart = driver.find_element(By.ID, "shopping_cart_container")
    
     def clickOnCart (self):
        self.Cart.click()