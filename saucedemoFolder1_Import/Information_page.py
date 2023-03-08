from selenium.webdriver.common.by import By

def Information(driver, firstName, lastName, cp):
    informationFirstName = driver.find_element(By.ID, "first-name")
    informationFirstName.send_keys(firstName)
    informationLastName = driver.find_element(By.ID, "last-name")
    informationLastName.send_keys(lastName)
    informationCodigoPostal = driver.find_element(By.ID, "postal-code")
    informationCodigoPostal.send_keys(cp)