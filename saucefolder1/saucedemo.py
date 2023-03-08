
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

options = webdriver.ChromeOptions()
options.add_argument("no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=400,600")
options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
time.sleep(1)

elem = driver.find_element(By.ID,"user-name")
elem.send_keys("standard_user")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, "password")
elem.send_keys("secret_sauce")
elem.send_keys(Keys.RETURN)

Btnlogin = driver.find_element(By.ID, "login-button").click()

bacpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
CamperaRoja = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(1)
contenedorCarrito = driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(1)

checkoutCompra = driver.find_element(By.ID, "checkout").click()
time.sleep(1)

informationFirstName = driver.find_element(By.ID, "first-name")
informationFirstName.send_keys("jeronimo")
time.sleep(1)

informationLastName = driver.find_element(By.ID, "last-name")
informationLastName.send_keys("tomas")
time.sleep(1)

informationCodigoPostal = driver.find_element(By.ID, "postal-code")
informationCodigoPostal.send_keys("5519")
time.sleep(1)

continuar = driver.find_element(By.ID, "continue").click()
time.sleep(1)

Finish = driver.find_element(By.ID,"finish").click()
time.sleep(1)
assert "Checkout: Complete!" in driver.page_source


BackHome = driver.find_element(By.ID, "back-to-products").click()
time.sleep(1)
driver.quit()


#ordernar por a-z
#producto1 = elem.find_element(By.XPATH,"text=Sauce Labs Backpack")
#padre =producto1.find_element(By.XPATH,"padre")
#padre.find_element(By.CLASS_NAME,"btn_inventory").click()
