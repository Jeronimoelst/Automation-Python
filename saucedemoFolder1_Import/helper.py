from selenium.webdriver.common.by import By

def clickButtonByName(driver, ButtonName):
    driver.find_element(By.NAME, ButtonName).click()

def VerifyText (driver, Text):
    assert Text in driver.page_source