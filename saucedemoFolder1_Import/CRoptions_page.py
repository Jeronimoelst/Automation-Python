from selenium import webdriver 


def setCRoptions():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sanbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("page load strategy")
    options.add_argument("--disable-web-security")
    options.add_argument("pageLoadStrategy")
    driver = webdriver.Chrome(options=options)
    return driver
