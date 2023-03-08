from Helpers.CROhelpersFlashScore import ChromeOptionsFSClass
from Helpers.HelpersFlashScore import HelpersFSClass
from Helpers.ScreenshotsFlashScore import ScreenshotErrorclass
from PageObject.SearchClub import SearchClubClass
from PageObject.Club_Deporte import SeleccionCDclass
import time

class SCclass:
    def __init__(self):
       pass

    def searchClubDep(self):
        CR = ChromeOptionsFSClass()
        driver = CR.setCRoptions()
        HFS = HelpersFSClass(driver)
        HFS.OpenBrowser("https://www.flashscore.com.ar/")
        time.sleep(10)
        HFS.clickButtonById("onetrust-accept-btn-handler")
        Search = SearchClubClass(driver)
        Search.Click()
        time.sleep(2)
        CR.QuitBrowser(driver)


    def SeleccionCD(self):
        CR = ChromeOptionsFSClass()
        driver = CR.setCRoptions()
        HFS = HelpersFSClass(driver)
        HFS.OpenBrowser("https://www.flashscore.com.ar/")
        time.sleep(8)
        HFS.clickButtonById("onetrust-accept-btn-handler")
        Search = SearchClubClass(driver)
        Search.Clicklupita()
        time.sleep(2)
        SCD = SeleccionCDclass(driver)
        SCD.InformationCS("Argentina")
        SCD.ElegirDeportes("Balonmano")
        SCD.TipodeEquipo("Argentina Sub-21")
        time.sleep(4)
        print(SCD.resultados())
        CR.QuitBrowser(driver)




testSC = SCclass()   
# testSC.searchClubDep()
testSC.SeleccionCD()