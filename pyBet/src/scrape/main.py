# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:14:31 2021

@author: p.zanghi
"""
import pandas
from direttaParser_2 import *
from time import time

if __name__ == "__main__":
    start = time()
    campionato = "Bundesliga"
    sito = DirettaP()
    sito.search(campionato, "l")  # cerca una squadra(t) o un compionato (l) o una partita (m)
    sito.openArchivio("2017/2018") #last 2017/2018 #if not archivio comment this line
    sito.tabular.clickRisultati(sito.driver)  # clicca la tab a seconda di cosa ci serve ed a seconda di cosa stia cercando (m,l,t)
    sito.showAllMatches() #clicca su mostra altro al massimo tre volte se c'è altro da mostrare
    sito.wait()
    openMatchByIDandRetakeData(sito, campionato)
    sito.quit()
    print((time() - start)/3600)


