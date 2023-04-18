from Helpers.ChromeOptionsDC import chromeOptionsDCClass
from Helpers.helpersDC import HelpersDCClass
from pageObjects.blog import blogClass
from pageObjects.mismatches import mismatchesClass
from pageObjects.proposal import proposalClass
import time

class dcClass:
    def __init__(self):
       pass

    def openBlogDC(self):
            chromeoptions = chromeOptionsDCClass()
            driver = chromeoptions.setCRoptions()
            helpersDC = HelpersDCClass(driver)
            helpersDC.OpenBrowser("https://desajustecreativo.com/")
            blog = blogClass(driver)
            blog.Click()
            time.sleep(2)
            chromeoptions.QuitBrowser(driver)

    def openProposalDC(self):
            chromeoptions = chromeOptionsDCClass()
            driver = chromeoptions.setCRoptions()
            helpersDC = HelpersDCClass(driver)
            helpersDC.OpenBrowser("https://desajustecreativo.com/")
            proposal = proposalClass(driver)
            proposal.Click()
            time.sleep(2)
            chromeoptions.QuitBrowser(driver)

    def openMismatchesDC(self):
            chromeoptions = chromeOptionsDCClass()
            driver = chromeoptions.setCRoptions()
            helpersDC = HelpersDCClass(driver)
            helpersDC.OpenBrowser("https://desajustecreativo.com/")
            mismatches = mismatchesClass(driver)
            mismatches.Click()
            time.sleep(2)
            chromeoptions.QuitBrowser(driver)

tests = dcClass() 
tests.openBlogDC()
# tests.openMismatchesDC()
# tests.openProposalDC