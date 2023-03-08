from selenium.webdriver.common.by import By

class BtnMenuLatclass:
    pageUrl = "https://www.saucedemo.com/inventory.html"


    def __init__(self, driver):
        #add implicit waits
        self.BtnItems = driver.find_element(By.ID, "react-burger-menu-btn")

        
    def BtnI(self):
        self.BtnItems.click()
 