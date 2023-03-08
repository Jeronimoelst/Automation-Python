from Helpers.CRhelper import ChromeOptionsClass
from PageObject.Login_page import LoginPageClass
from PageObject.Cart_page import CartClass
from PageObject.About_page import Aboutclass
from PageObject.Information_page import InformationPageClass
from Helpers.helper import HelpersClass
from PageObject.BtnMenuLateral_page import BtnMenuLatclass
from PageObject.ItemsMenuLateral import ItemsMenuLatclass
from Helpers.Screenshot import ScreenshotErrorclass
import time

class Testing:

    def testCompra():
        #Open Browser
        driver = ChromeOptionsClass.setCRoptions()
        helper = HelpersClass(driver)
        helper.OpenBrowser(LoginPageClass.pageUrl)
        #login
        login=LoginPageClass(driver)
        login.Login("performance_glitch_user" , "secret_sauce")
        helper.clickButtonByName("login-button")
        helper.VerifyText ("Products")
        #select products
        helper.clickButtonByName ("add-to-cart-sauce-labs-backpack")
        helper.clickButtonByName ("add-to-cart-sauce-labs-bike-light")
        helper.clickButtonByName ("add-to-cart-sauce-labs-bolt-t-shirt")
        helper.clickButtonByName ("add-to-cart-sauce-labs-fleece-jacket")
        cartPage= CartClass(driver)
        #navigate to cart page
        cartPage.clickOnCart()
        helper.VerifyText("Your Cart")
        helper.clickButtonByName("remove-sauce-labs-backpack")
        helper.clickButtonByName("remove-sauce-labs-bike-light")
        helper.clickButtonByName("checkout")
        # Purchase Data
        information = InformationPageClass(driver)
        information.Information("juan", "agustin", 3455)
        helper.clickButtonByName("continue")
        helper.VerifyText("Checkout: Overview")
        helper.clickButtonByName("finish")
        # Checkout
        helper.VerifyText("Checkout: Complete!") 
        # Back to Products
        helper.clickButtonByName("back-to-products")
        helper.VerifyText("Products") 
        driver.quit()

    def TestUrl(): 
        # Open Browser
         driver = ChromeOptionsClass.setCRoptions()
         testhelper = HelpersClass(driver)
        #  Navigate to Url
         testhelper.NavegationTo(Aboutclass.pageurl)
         driver.quit()

    def TestMenuLat():
        # Open Browser
        driverc = ChromeOptionsClass()
        driver = driverc.setCRoptions()
        helper = HelpersClass(driver)
        helper.OpenBrowser(LoginPageClass.pageUrl)
        # Login
        login=LoginPageClass(driver)
        login.Login("performance_glitch_user" , "secret_sauce")
        helper.clickButtonByName("login-button")
        # Page
        helper.VerifyText ("Products")
        # Lateral Menu
        btn = BtnMenuLatclass(driver)
        btn.BtnI()
        # Go to Items
        Items = ItemsMenuLatclass(driver)
        Items.ClickItemsAbout()
        #quit browser
        driverc.QuitBrowser(driver)




    def TestFail():
     try:
         # Open Browser
        driverc = ChromeOptionsClass()
        driver = driverc.setCRoptions()
        helper = HelpersClass(driver)
        helper.OpenBrowser(LoginPageClass.pageUrl)
        # Login
        login=LoginPageClass(driver)
        login.Login("performance_glitch_user" , "secret_sauces")
        helper.clickButtonByName("login-button")
         # Page
        helper.VerifyText ("Products")
     except:
        print("failed, look at the scrennshoot")
        Screen = ScreenshotErrorclass()
        Screen.ScreenS(driver)
     finally:   
        #quit browser
        driverc.QuitBrowser(driver)
       
         


# Testing.testCompra()
Testing.TestUrl()
# Testing.TestMenuLat()
# Testing.TestFail()