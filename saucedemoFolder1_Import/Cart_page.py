from selenium.webdriver.common.by import By

def Cart (driver, Cart):
    driver.find_element(By.ID, Cart).click()