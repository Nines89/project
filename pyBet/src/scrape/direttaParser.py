# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:48:31 2021

@author: Nines8989
"""
from time import sleep, time
from selenium import webdriver
from sys import exit
import retakeData
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.db.dataBase import Excel

macroTab = "PARTITA"

class leagueTab:
    def __init__(self):
        self.riepilogo = "li0"
        self.risultati = "li1"
        self.calendario = "li2"
        self.classifiche = "li3"
        self.archivio = "li4"

    def clickRiepilogo(self, driver):
        driver.find_element(By.ID, self.riepilogo).click()

    def clickRisultati(self, driver):
        driver.find_element(By.ID, self.risultati).click()

    def clickCalendario(self, driver):
        driver.find_element(By.ID, self.calendario).click()

    def clickClassifiche(self, driver):
        driver.find_element(By.ID, self.classifiche).click()

    def clickArchivio(self, driver):
        driver.find_element(By.ID, self.archivio).click()


class teamTab:
    def __init__(self):
        self.riepilogo = "li0"
        self.news = "li1"
        self.risultati = "li2"
        self.calendario = "li3"
        self.classifiche = "li4"
        self.trasferimenti = "li5"
        self.rosa = "li6"

    def clickRiepilogo(self, driver):
        driver.find_element(By.ID, self.riepilogo).click()

    def clickNews(self, driver):
        driver.find_element(By.ID, self.news).click()

    def clickRisultati_team(self, driver):
        driver.find_element(By.ID, self.risultati).click()

    def clickCalendario(self, driver):
        driver.find_element(By.ID, self.calendario).click()

    def clickClassifiche(self, driver):
        driver.find_element(By.ID, self.classifiche).click()

    def clickTrasferimenti(self, driver):
        driver.find_element(By.ID, self.trasferimenti).click()

    def clickRosa(self, driver):
        driver.find_element(By.ID, self.rosa).click()


class matchTab:
    def __init__(self):
        self.partita = "PARTITA"
        self.quote = "COMPARAZIONE QUOTE"
        self.TaT = "TESTA A TESTA"
        self.classifiche = "CLASSIFICHE"

    # element has to be a string with the child tab name
    def clickPartita(self, driver, element):
        cli_elem = [
            "INFORMAZIONI PARTITA",
            "STATISTICHE",
            "FORMAZIONI"
        ]
        global macroTab
        if macroTab != "PARTITA":
            try:
                driver.find_element_by_link_text(self.partita).click()
                macroTab = "PARTITA"
            finally:
                pass

        if element not in cli_elem:
            print("qui: CHILD TAB INESISTENTE: ")
        else:
            try:
                driver.find_element_by_link_text(element).click()
            finally:
                pass

    def clickQuote(self, driver, element):
        cli_elem = [
            "1 X 2",
            "O/U",
            "DC",
            "GOL"
        ]

        global macroTab
        if macroTab != "COMPARAZIONE QUOTE":
            try:
                driver.find_element_by_link_text(self.quote).click()
                macroTab = "COMPARAZIONE QUOTE"
            finally:
                pass

        if element not in cli_elem:
            print("CHILD TAB INESISTENTE")
        else:
            try:
                driver.find_element_by_link_text(element).click()
            finally:
                pass

    def clickTaT(self, driver, element):
        cli_elem = [
            "TOTALE",
            "- CASA",
            "- FUORI"
        ]

        global macroTab
        if macroTab != "TESTA A TESTA":
            try:
                driver.find_element_by_link_text(self.TaT).click()
                macroTab = "TESTA A TESTA"
            finally:
               pass

        if element not in cli_elem:
            print("CHILD TAB INESISTENTE")
        else:
            try:
                driver.find_element_by_partial_link_text(element).click()
            finally:
                pass

    def clickClassifiche(self, driver, element, value="0"):
        cli_elem = [
            "CLASSIFICHE",
            "FORMA",
            "OVER/UNDER"
        ]

        global macroTab
        if macroTab != "CLASSIFICHE":
            try:
                driver.find_element_by_link_text(self.classifiche).click()
                macroTab = "CLASSIFICHE"
            finally:
                pass

        if element not in cli_elem:
            print("CHILD TAB INESISTENTE")
        else:
            try:
                driver.find_element_by_link_text(element).click()
                if element == "FORMA":
                    driver.find_element_by_link_text("10").click()
                if element == "OVER/UNDER":
                    if value != "0":
                        driver.find_element_by_link_text(value).click()
            except:
                if element == "OVER/UNDER":
                    if value != "0":
                        driver.find_element_by_link_text(value).click()
                pass


class DirettaP:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(r"https://www.diretta.it/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.tabular = None
        self.league = None

    def search(self, word, tab):
        def tabata(tab):
            # tab is a letter l = league || t = team || m = match
            if tab == "l":
                self.tabular = leagueTab()
                self.league = word
            elif tab == "t":
                self.tabular = teamTab()
            elif tab == "m":
                self.tabular = matchTab()
            else:
                self.tabular = "Tab Inconsistente"
                exit()

        tabata(tab)
        self.driver.find_element_by_class_name("searchIcon").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CLASS_NAME, "searchInput__input").send_keys(word + Keys.ENTER)
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CLASS_NAME, "searchResult").click()

    def showAllMatches(self):
        essence = True
        count = 0
        while essence:
            count += 1
            if count > 4:
                essence = False
            try:
                self.driver.implicitly_wait(30)
                sleep(1)
                self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
                self.driver.implicitly_wait(30)
                self.driver.find_element_by_link_text("Mostra più incontri").click()
            except NoSuchElementException:
                essence = False

    def getPage(self):
        return self.driver.page_source

    def nextWind(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    def lastPage(self):
        self.driver.back()

    def wait(self):
        self.driver.implicitly_wait(30)

    def scrollOnTop(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

    def currentUrl(self):
        return self.driver.current_url

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


def openMatchByIDandRetakeData(page):
    matches = retakeData.find_IDs(page.getPage())
    tempo_uno = time()
    print("START MATCH")
    #a = 0 #TODO delete in final cut
    prevTab = page.tabular
    page.tabular = matchTab()
    tempo_due = time()
    print("trovati id: ", tempo_due - tempo_uno)
    for mat in matches:
        # excel
        f = Excel()
        f.openSheet(page.league)
        tempo_tre = time()
        print("dopo excel:", tempo_tre - tempo_due)
        try:
            global macroTab
            macroTab = "PARTITA"
            id_ = mat.group("ID")
            page.wait()
            page.scrollOnTop()
            page.wait()
            page.driver.find_element(By.ID, id_).click()
            page.wait()
            #a += 1 #TODO delete in final cut
            page.wait()
            page.nextWind(1)
            # rec statistiche and result starts
            page.wait()
            page.tabular.clickPartita(page.driver, "STATISTICHE")
            sleep(1)
            tempo_quattro = time()
            print("entra nella partita:", tempo_quattro - tempo_tre)
            common = retakeData.checkNormalMatch(page.getPage())
            if common and common == "Giornata":
                result = retakeData.PageResult(page.getPage())
                result.find_stat()
                page.wait()
                # rec num infortunati
                page.tabular.clickPartita(page.driver, "FORMAZIONI")
                sleep(1)
                result.txt = page.getPage()
                result.find_infortunati()
                page.wait()
                # rec pt/st reusults
                page.tabular.clickPartita(page.driver, "INFORMAZIONI PARTITA")
                sleep(1)
                result.txt = page.getPage()
                result.find_ptResults()
                result.find_stResults()
                page.wait()
                # rec quote uo
                page.tabular.clickQuote(page.driver, "O/U")
                sleep(1)
                result.txt = page.getPage()
                result.find_quote_UO()
                page.wait()
                # rec quote1x2
                page.tabular.clickQuote(page.driver, "1 X 2")
                sleep(1)
                result.txt = page.getPage()
                result.find_quote_1x2()
                page.wait()
                # rec quote dc
                page.tabular.clickQuote(page.driver, "DC")
                sleep(1)
                result.txt = page.getPage()
                result.find_quote_DC()
                page.wait()
                # rec quote gg
                page.tabular.clickQuote(page.driver, "GOL")
                sleep(1)
                result.txt = page.getPage()
                result.find_quote_GG()
                page.wait()
                # rec TaT Casa
                page.tabular.clickTaT(page.driver, "- CASA")
                sleep(1)
                result.txt = page.getPage()
                result.lm_CASA_match()
                page.wait()
                # rec TaT trasferta
                page.tabular.clickTaT(page.driver, "- FUORI")
                sleep(1)
                result.txt = page.getPage()
                result.lm_TRANSFERTA_match()
                page.wait()
                # rec TaT totale
                page.tabular.clickTaT(page.driver, "TOTALE")
                sleep(1)
                result.txt = page.getPage()
                result.find_last_match()
                page.wait()
                # rec pos classifica
                page.tabular.clickClassifiche(page.driver, "CLASSIFICHE")
                sleep(1)
                result.txt = page.getPage()
                result.find_classifica()
                page.wait()
                # rec forma
                page.tabular.clickClassifiche(page.driver, "FORMA")
                sleep(1)
                result.txt = page.getPage()
                result.find_forma()
                page.wait()
                # rec num over/under
                page.tabular.clickClassifiche(page.driver, "OVER/UNDER", "0.5")
                sleep(1)
                result.txt = page.getPage()
                result.n_Over_Under_05()
                page.wait()
                page.tabular.clickClassifiche(page.driver, "OVER/UNDER", "1.5")
                sleep(1)
                result.txt = page.getPage()
                result.n_Over_Under_15()
                page.wait()
                page.tabular.clickClassifiche(page.driver, "OVER/UNDER", "2.5")
                sleep(1)
                result.txt = page.getPage()
                result.n_Over_Under_25()
                page.wait()
                page.tabular.clickClassifiche(page.driver, "OVER/UNDER", "3.5")
                sleep(1)
                result.txt = page.getPage()
                result.n_Over_Under_35()
                page.wait()
                page.tabular.clickClassifiche(page.driver, "OVER/UNDER", "4.5")
                sleep(1)
                result.txt = page.getPage()
                result.n_Over_Under_45()
                page.wait()
                tempo_cinque = time()
                print("prima excel: ", tempo_cinque - tempo_quattro)

                # excel
                f.writeRow(result)
                f.saveCVS()

                tempo_sei = time()
                print("dopo excel: ", tempo_sei - tempo_cinque)

            delPage = page
            delPage.close()
            page.nextWind(0)

            #if a == 2:    #TODO delete in final cut
            #    exit()
            tempo_sette = time()
            print("fine ciclo: ", tempo_sette - tempo_sei)
        finally:
            continue

    page.tabular = prevTab


def openArchivio(page, arc):
    page.tabular.clickArchivio(page.driver)
    page.wait()
    page.driver.find_element_by_partial_link_text(arc).click()
    page.wait()


if __name__ == "__main__":
    sito = DirettaP()
    sito.search("Ligue 1", "l")  # cerca una squadra(t) o un compionato (l) o una partita (m)
    #openArchivio(sito, "2020/2021")
    sito.tabular.clickRisultati(sito.driver)  # clicca la tab a seconda di cosa ci serve ed a seconda di cosa stia cercando (m,l,t)
    # sito.showAllMatches()  # clicca su mostra altro al massimo tre volte se c'è altro da mostrare
    sito.wait()
    pageSourch = sito.getPage()  # contiene la str del codice html della pagina in considerazione
    openMatchByIDandRetakeData(sito)
    # sito.tabular.clickRisultati(sito.driver) #clicca la tab a seconda di cosa ci serve ed a seconda di cosa stia cercando (m,l,t)
    # sito.showAllMatches() #clicca su mostra altro al massimo tre volte se c'è altro da mostrare
    # pageSourch = sito.getPage() #contiene la str del codice html della pagina in considerazione
    # openMatchByIDandRetakeData(sito)
    sito.quit()



