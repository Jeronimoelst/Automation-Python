from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchClubClass:
    
    def __init__(self, driver):
        pageUrl = "https://www.flashscore.com.ar/"
        wait = WebDriverWait(driver, 10)
        self.SearchW = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, 'search-window')))

    def Clicklupita(self):
        self.SearchW.click()