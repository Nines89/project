from time import sleep, time
from selenium import webdriver
from sys import exit
import retakeData
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dataBase import Excel

class LeagueTab:
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

class TeamTab:
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


class DirettaP:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(r"https://www.diretta.it/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.tabular = None
        self.league = None

    def search(self, word, tab):
        def tabata(tab):
            # tab is a letter l = league || t = team
            if tab == "l":
                self.tabular = LeagueTab()
                self.league = word
            elif tab == "t":
                self.tabular = TeamTab()
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

    def openArchivio(self, arc):
        self.tabular.clickArchivio(self.driver)
        self.wait()
        self.driver.find_element_by_partial_link_text(arc).click()

class Match:
    def __init__(self, driver):
        self.driver = driver
        self.tab = 0

    def clickPartita(self):
        self.driver.find_element_by_link_text("PARTITA").click()
        self.tab = 0

    def clickInfoPartita(self):
        if self.tab == 0:
            self.driver.find_element_by_link_text("INFORMAZIONI PARTITA").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickStatistiche(self):
        if self.tab == 0:
            self.driver.find_element_by_link_text("STATISTICHE").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickFormazioni(self):
        if self.tab == 0:
            self.driver.find_element_by_link_text("FORMAZIONI").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickQuote(self):
        self.driver.find_element_by_link_text("COMPARAZIONE QUOTE").click()
        self.tab = 1

    def click1x2(self):
        if self.tab == 1:
            self.driver.find_element_by_link_text("1 X 2").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickUO(self):
        if self.tab == 1:
            self.driver.find_element_by_link_text("O/U").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickDC(self):
        if self.tab == 1:
            self.driver.find_element_by_link_text("DC").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickGOAL(self):
        if self.tab == 1:
            self.driver.find_element_by_link_text("GOL").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickTAT(self):
        self.driver.find_element_by_link_text("TESTA A TESTA").click()
        self.tab = 2

    def clickTATtotale(self):
        if self.tab == 2:
            self.driver.find_element_by_link_text("TOTALE").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickTATcasa(self):
        if self.tab == 2:
            self.driver.find_element_by_partial_link_text("CASA").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickTATfuori(self):
        if self.tab == 2:
            self.driver.find_element_by_partial_link_text("FUORI").click()
        else:
            raise "tab errata per l'evento richiesto"

    '''classifiche contiene anche la pagina delle classifiche vere e proprie'''
    def clickClass(self):
        self.driver.find_element_by_link_text("CLASSIFICHE").click()
        self.tab = 3

    def clickForma(self):
        if self.tab == 3:
            self.driver.find_element_by_link_text("FORMA").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickFormaUO(self):
        if self.tab == 3:
            self.driver.find_element_by_link_text("OVER/UNDER").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickFormaUO05(self):
        if self.tab == 3:
            self.driver.find_element_by_link_text("0.5").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickFormaUO15(self):
        if self.tab == 3:
            self.driver.find_element_by_link_text("1.5").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickFormaUO25(self):
        if self.tab == 3:
            self.driver.find_element_by_link_text("2.5").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickFormaUO35(self):
        if self.tab == 3:
            self.driver.find_element_by_link_text("3.5").click()
        else:
            raise "tab errata per l'evento richiesto"

    def clickFormaUO45(self):
        if self.tab == 3:
            self.driver.find_element_by_link_text("4.5").click()
        else:
            raise "tab errata per l'evento richiesto"

def openMatchByIDandRetakeData(page):
    matches = retakeData.find_IDs(page.getPage())
    for mat in matches:
        #f = Excel()
        #f.openSheet(page.league)
        id_ = mat.group("ID")
        page.scrollOnTop()
        page.wait()
        page.driver.find_element(By.ID, id_).click()
        page.wait()
        page.nextWind(1)
        common = retakeData.checkNormalMatch(page.getPage())
        if common and common == "Giornata":
            '''crea la variabile per la raccolta dati'''
            result = retakeData.PageResult(page.getPage())
            '''crea la partita'''
            partita = Match(page.driver)
            page.wait()
            '''rec statistiche'''
            partita.clickStatistiche()
            sleep(1)
            result.txt = page.getPage()
            result.find_stat()

            '''rec infortunati'''
            partita.clickFormazioni()
            sleep(1)
            result.txt = page.getPage()
            result.find_infortunati()

            '''rec pt/st result'''
            partita.clickInfoPartita()
            sleep(1)
            result.txt = page.getPage()
            result.find_ptResults()
            result.find_stResults()
            page.wait()

            ''' rec quote uo'''
            partita.clickQuote()
            page.wait()
            partita.clickUO()
            sleep(1)
            result.txt = page.getPage()
            result.find_quote_UO()
            page.wait()

            '''rec quote 1x2'''
            partita.click1x2()
            sleep(1)
            result.txt = page.getPage()
            result.find_quote_1x2()
            page.wait()

            '''rec quote dc'''
            partita.clickDC()
            sleep(1)
            result.txt = page.getPage()
            result.find_quote_DC()
            page.wait()

            '''rec quote gg'''
            partita.clickGOAL()
            sleep(1)
            result.txt = page.getPage()
            result.find_quote_GG()
            page.wait()

            '''rec TaT totale'''
            partita.clickTAT()
            sleep(1)
            result.txt = page.getPage()
            result.find_last_match()
            page.wait()

            '''rec TaT Casa'''
            partita.clickTATcasa()
            sleep(1)
            result.txt = page.getPage()
            result.lm_CASA_match()
            page.wait()

            '''rec TaT Trasferta'''
            partita.clickTATfuori()
            sleep(1)
            result.txt = page.getPage()
            result.lm_TRANSFERTA_match()
            page.wait()

            '''rec pos classifica'''
            partita.clickClass()
            sleep(1)
            result.txt = page.getPage()
            result.find_classifica()
            page.wait()

            '''rec forma'''
            partita.clickForma()
            sleep(1)
            result.txt = page.getPage()
            result.find_forma()
            page.wait()

            '''tab over/under'''
            partita.clickFormaUO()
            sleep(1)

            '''rec num over/under 0.5'''
            partita.clickFormaUO05()
            sleep(1)
            result.txt = page.getPage()
            result.n_Over_Under_05()
            page.wait()

            '''rec num over/under 1.5'''
            partita.clickFormaUO15()
            sleep(1)
            result.txt = page.getPage()
            result.n_Over_Under_15()
            page.wait()

            '''rec num over/under 2.5'''
            partita.clickFormaUO25()
            sleep(1)
            result.txt = page.getPage()
            result.n_Over_Under_25()
            page.wait()

            '''rec num over/under 3.5'''
            partita.clickFormaUO35()
            sleep(1)
            result.txt = page.getPage()
            result.n_Over_Under_35()
            page.wait()

            '''rec num over/under 4.5'''
            partita.clickFormaUO45()
            sleep(1)
            result.txt = page.getPage()
            result.n_Over_Under_45()
            page.wait()

            # excel
            #f.writeRow(result)
            #f.saveCVS()

        delPage = page
        delPage.close()
        page.nextWind(0)





if __name__ == "__main__":
    c = DirettaP()
    c.search("Serie A", "l")
    c.openArchivio("2019/2020")
    c.tabular.clickRisultati(c.driver)
    openMatchByIDandRetakeData(c)
