

from greatings import greets

# title mi sa che mette le prime lettere in maiuscolo
for g in greets:
    print(f"{g.title()} versus {g}")

"""
Per prima cosa andiamo su VCS dalla lista di Pycharm in alto
 - click su Enable Version Control Integration
 - nel menù a tendina che comparirà segnamo git
 - accanto a project comparirà una nuova tab definita: Commit
 - per aggiungere un nuovo file a git, tasto dx su di esso (main.py) -> Git -> Add
 - il nome del file, dopo aver fatto l'add diventerà da rosso a verde.
 - per committare i cambiamenti vai nella tab commit
 - ricorda la differenza in questa zona tra aggiunti e non
 - selezionare i file aggiunti per committare i cambiamenti
 - creare un commento e cliccare su Commit
 - i file committati torneranno in verde, finchè, una volta rimodificati torneranno in blu

Storia dei commit:
 - Vai nella barra in basso, dove c'è il terminale, clicca su Git e ci sarà nella tab log l'elenco
 - click su un commit, tasto destro su uno dei file del commit --> compare with local
 
 Tornare ad una versione precedente del programma:
  - Andare nei log come visto prima
  - cliccare stavolta con il dx sul commit e non sul file
  - "reset current brench to here"
  - scegliere l'opzione desiderata (soft - mixed- hard keep)
  - attenzione: con hard i commit successivi a quello scelto saranno eliminati
  - per vedere le differenze si potrebbe dover chiudere e riaprire il file in questione
  
 Vediamo come integrare il tutto con git-hub per averlo anche online:
  - vai su File -> Settings -> Version Control -> GitHub
  - effetta il log in premendo sul +
  - adesso che abbiamo collegato il nostro account leghiamo questo progetto ad un repository personale
  - freccia verde in alto a dx (push) -> define remote
  - incolla il nome del repo e vai su push
"""