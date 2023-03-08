
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome() #agregar capabilities
driver.get("https://www.google.com")
time.sleep(5)
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("youtube")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
