from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleccionCDclass:


    def __init__(self, driver):

        pageUrl = "https://www.flashscore.com.ar/"

        wait = WebDriverWait(driver, 20)

        self.driver=driver

        self.Input_Busqueda = driver.find_element(By.CLASS_NAME, "searchInput__input")
        self.ListaDesplegable = wait.until(EC.element_to_be_clickable(driver.find_element(By.CLASS_NAME, 'dropdown__selectedValue')))


    def InformationCS(self , Club):
        self.Input_Busqueda.click()
        self.Input_Busqueda.send_keys(Club)
        self.Input_Busqueda.send_keys(Keys.RETURN)

        
    def ElegirDeportes(self, deporte):
        time.sleep(1)
        self.ListaDesplegable.click()
        time.sleep(1)
        ListaDesplegableS = self.driver.find_elements(By.CLASS_NAME, 'dropdown__option')
        for elemento in ListaDesplegableS:
            # print(elemento.text)
            if elemento.text == deporte:
                elemento.click()
                break
        time.sleep(2)       


    def TipodeEquipo(self, equipo):
        TipoE = self.driver.find_elements(By.CLASS_NAME, 'searchResult__participantName')
        for E in TipoE:
            # print(E.text)
            if E.text == equipo:
                E.click()
                break
        time.sleep(2)

        
    def resultados(self):
        resultados=[]
        time.sleep(7)
        Partidos = self.driver.find_elements(By.CLASS_NAME, 'event__match--twoLine')
        for Partido in Partidos:
            fecha =Partido.find_element(By.CLASS_NAME, "event__time")
            local= Partido.find_element(By.CLASS_NAME,"event__participant--home")
            resLocal = Partido.find_element(By.CLASS_NAME, "event__score--home")   
            visitante = Partido.find_element(By.CLASS_NAME,"event__participant--away")
            resVisitante = Partido.find_element(By.CLASS_NAME, "event__score--away")   
            resultados.append(fecha.text)
            resultados.append(local.text)
            resultados.append(resLocal.text)
            resultados.append(visitante.text)
            resultados.append(resVisitante.text)

        return resultados
        