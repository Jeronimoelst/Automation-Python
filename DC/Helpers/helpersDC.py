from selenium.webdriver.common.by import By


class HelpersDCClass:
    def __init__(self,driver):
        self.driver = driver

    def clickButtonByName(self, ButtonName):
        self.driver.find_element(By.NAME, ButtonName).click()

    def VerifyText (self, Text):
        assert Text in self.driver.page_source

    def OpenBrowser(self, page_url):
        self.driver.get(page_url)

    def NavegationTo(self, pageUrl):
        self.driver.get(pageUrl)

    def clickButtonById(self, ById):
        self.driver.find_element(By.ID, ById).click()
