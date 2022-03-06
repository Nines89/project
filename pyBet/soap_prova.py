import requests
from bs4 import BeautifulSoup
import csv

if __name__=="__main__":
    URL = "http://www.diretta.it"
    r = requests.get(URL)

    print(r)

