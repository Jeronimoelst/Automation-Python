from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class mismatchesClass:
    

     def __init__(self, driver):
        pageUrl = "https://desajustecreativo.com/"
        wait = WebDriverWait(driver, 3)
        self.mismatchesseccion = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '/html/body/header/div/nav/a[4]')))

     def clickmismatches(self):
        self.mismatchesseccion.click()