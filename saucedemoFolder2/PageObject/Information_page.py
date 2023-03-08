
from selenium.webdriver.common.by import By



class InformationPageClass:
    

      def __init__(self, driver):
        self.pageUrl = "https://www.saucedemo.com/checkout-step-one.html"
         #add implicit waits
        self.informationFirstName = driver.find_element(By.ID, "first-name")
        self.informationLastName = driver.find_element(By.ID, "last-name")
        self.informationCodigoPostal = driver.find_element(By.ID, "postal-code")
        
      def Information(self, firstName, lastName, cp):

        self.informationFirstName.send_keys(firstName)
        self.informationLastName.send_keys(lastName)
        self.informationCodigoPostal.send_keys(cp)