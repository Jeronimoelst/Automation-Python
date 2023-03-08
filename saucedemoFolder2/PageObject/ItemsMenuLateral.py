from selenium.webdriver.common.by import By

class ItemsMenuLatclass:
    pageUrl = "https://www.saucedemo.com/inventory.html"


    def __init__(self, driver):
         #add implicit waits
        self.AllItems = driver.find_element(By.ID, "inventory_sidebar_link")
        self.About = driver.find_element(By.ID, "about_sidebar_link")
        self.Logout = driver.find_element(By.ID, "logout_sidebar_link")
        self.ResetAppState = driver.find_element(By.ID, "reset_sidebar_link")

    def ClickItemsAll(self):
        self.AllItems.click()

    def ClickItemsAbout(self):
        self.About.click()
        
    def ClickItemsLogout(self):
        self.Logout.click()

    def ClickItemsReset(self):
        self.ResetAppState.click()
