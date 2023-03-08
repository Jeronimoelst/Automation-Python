from selenium import webdriver
from datetime import datetime
import os

class ScreenshotErrorclass:

    def __init__(self):
        pass


    def ScreenS(self, driver):
        try:
            now = datetime.now()
            name= "Screenshot" + str(now.day) + str(now.month) + str(now.minute) + ".png"
            fullpath=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
            driver.save_screenshot(fullpath+"/screeNshot/"+ name) 
        except Exception as e:
            print(e)
