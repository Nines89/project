

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
 - 
"""