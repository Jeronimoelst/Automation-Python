from selenium import webdriver 


class ChromeOptionsFSClass:
    def __init__(self):
         pass

    def setCRoptions(self):
            options = webdriver.ChromeOptions()
            options.add_argument("no-sanbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-web-security")
            driver = webdriver.Chrome(options=options)
            return driver

    def QuitBrowser(self, driver):
        driver.quit()  
