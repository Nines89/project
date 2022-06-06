from src.db.dataBase import Excel
import os
from src.scrape.retakeData import last_regex, last_regex_vsv
from datetime import date
import csv

i = 0


def last_matches_adapt(stringa, vsv=False):
    '''
    Def of a function = def last_matches_adapt() -> Dict[int, float]
    :param stringa: la stringa dei risultati da trasformare
    :param vsv: il flag per determinare se viene trattata la stringa senza l'esito
    :return: dizionario contenente le percentuali degli ultimi scontri
    '''
    percent_vittoria = 0
    percent_pareggio = 0
    percent_sconfitta = 0
    percent_over = 0
    percent_under = 0
    if vsv == False:
        goal1, goal2, esito = last_regex(stringa)
    else:
        goal1, goal2 = last_regex_vsv(stringa)

    for ix in range(len(goal1)):
        tot = goal2[ix] + goal1[ix]
        if tot < 2.5:
            percent_under += 1
        else:
            percent_over += 1
    if vsv == False:
        for e in esito:
            if e == 'P':
                percent_sconfitta += 1
            elif e == 'V':
                percent_vittoria += 1
            else:
                percent_pareggio += 1
    else:
        for id in range(len(goal1)):
            if goal2[id] > goal1[id]:
                percent_sconfitta += 1
            elif goal2[id] < goal1[id]:
                percent_vittoria += 1
            else:
                percent_pareggio += 1

    percent_vittoria = percent_vittoria/5*100
    percent_sconfitta = percent_sconfitta / 5 * 100
    percent_pareggio = percent_pareggio / 5 * 100
    percent_under = percent_under/5*100
    percent_over = percent_over/5*100

    return {1: percent_vittoria, 2: percent_pareggio, 3: percent_sconfitta,
            4: percent_over, 5: percent_under}


def modifi_match(array):
    """
    Def of a function = def modifi_match(array: {__len__, __getitem__}) -> list
    trasforma l'elemento page reuslt che viene dall'Excel in un array
    da usare per la NN

    :return: Lista
    Ogni lista contiene un elemento nel solito ordine impostato nella classe
    """

    todos = []
    for a in range(len(array)):
        arr = []
        arr.append(array[a].data)
        arr.append(array[a].team1)
        arr.append(array[a].team2)
        arr.append(array[a].classifica1)
        arr.append(array[a].classifica2)
        arr.append(array[a].forma1)
        arr.append(array[a].forma2)
        arr.append(array[a].goalPT1)
        arr.append(array[a].goalPT2)
        arr.append(array[a].goalST1)
        arr.append(array[a].goalST2)
        arr.append(array[a].totGoal1)
        arr.append(array[a].totGoal2)
        arr.append(array[a].totGoal)
        arr.append(array[a].possPalla1)
        arr.append(array[a].possPalla2)
        arr.append(array[a].tiri1)
        arr.append(array[a].tiri2)
        arr.append(array[a].tiriPorta1)
        arr.append(array[a].tiriPorta2)
        arr.append(array[a].tiriFuori1)
        arr.append(array[a].tiriFuori2)
        arr.append(array[a].tiriFermati1)
        arr.append(array[a].tiriFermati2)
        arr.append(array[a].Punizioni1)
        arr.append(array[a].Punizioni2)
        arr.append(array[a].Angolo1)
        arr.append(array[a].Angolo2)
        arr.append(array[a].FuoriGioco1)
        arr.append(array[a].FuoriGioco2)
        arr.append(array[a].Parate1)
        arr.append(array[a].Parate2)
        arr.append(array[a].Falli1)
        arr.append(array[a].Falli2)
        arr.append(array[a].Rossi1)
        arr.append(array[a].Rossi2)
        arr.append(array[a].Gialli1)
        arr.append(array[a].Gialli2)
        arr.append(array[a].Passaggi1)
        arr.append(array[a].Passaggi2)
        arr.append(array[a].Contrasti1)
        arr.append(array[a].Contrasti2)
        arr.append(array[a].Attacchi1)
        arr.append(array[a].Attacchi2)
        arr.append(array[a].AttacchiPer1)
        arr.append(array[a].AttacchiPer2)
        arr.append(array[a].NumInfortunati1)
        arr.append(array[a].NumInfortunati2)

        arr.append(array[a].quota1)
        arr.append(array[a].quotaX)
        arr.append(array[a].quota2)

        arr.append(array[a].numOver05_1)
        arr.append(array[a].numOver05_2)
        arr.append(array[a].numUnder05_1)
        arr.append(array[a].numUnder15_2)
        arr.append(array[a].numOver15_1)
        arr.append(array[a].numOver15_2)
        arr.append(array[a].numUnder15_1)
        arr.append(array[a].numUnder15_2)
        arr.append(array[a].numOver25_1)
        arr.append(array[a].numOver25_2)
        arr.append(array[a].numUnder25_1)
        arr.append(array[a].numUnder25_2)
        arr.append(array[a].numOver35_1)
        arr.append(array[a].numOver35_2)
        arr.append(array[a].numUnder35_1)
        arr.append(array[a].numUnder35_2)
        arr.append(array[a].numOver45_1)
        arr.append(array[a].numOver45_2)
        arr.append(array[a].numUnder45_1)
        arr.append(array[a].numUnder45_2)

        arr.append(array[a].quotaUnd05)
        arr.append(array[a].quotaOv05)
        arr.append(array[a].quotaUnd15)
        arr.append(array[a].quotaOv15)
        arr.append(array[a].quotaUnd25)
        arr.append(array[a].quotaOv25)
        arr.append(array[a].quotaUnd35)
        arr.append(array[a].quotaOv35)
        arr.append(array[a].quotaUnd45)
        arr.append(array[a].quotaOv45)

        arr.append(array[a].quota12)
        arr.append(array[a].quota1X)
        arr.append(array[a].quotaX2)

        arr.append(array[a].quotaGG)
        arr.append(array[a].quotaNG)

        add = last_matches_adapt(array[a].lastMatchs1)
        arr.append(add[1])
        arr.append(add[2])
        arr.append(add[3])
        arr.append(add[4])
        arr.append(add[5])
        add = last_matches_adapt(array[a].lastMatchs2)
        arr.append(add[1])
        arr.append(add[2])
        arr.append(add[3])
        arr.append(add[4])
        arr.append(add[5])
        add = last_matches_adapt(array[a].prevMatchsVS, True) #TODO DA PROVARE
        arr.append(add[1])
        arr.append(add[2])
        arr.append(add[3])
        arr.append(add[4])
        arr.append(add[5])
        add = last_matches_adapt(array[a].lastMatchsCASA)
        arr.append(add[1])
        arr.append(add[2])
        arr.append(add[3])
        arr.append(add[4])
        arr.append(add[5])
        add = last_matches_adapt(array[a].lastMatchsTRASFERTA)
        arr.append(add[1])
        arr.append(add[2])
        arr.append(add[3])
        arr.append(add[4])
        arr.append(add[5])

        todos.append(arr)

    return todos


def import_data():
    """
    Def of a function = def import_data() -> List[list]
    Importa i dati dalla specifica cartella allo stesso livello
    dello script

    :return: Lista di liste
    Il primo livello della lista contiene i campionati
    Il secondo livello della lista contiene la partita, dalla più moderna
    alla più antica
    """
    all_data = []
    root = './data'
    for file_name in os.listdir(root):
        file_path = os.path.join(root, file_name)
        if os.path.isdir(file_path) or file_name == 'data.xlsx':
            pass
        elif file_name.endswith(".xlsx"):
            file_name = file_name[0:-5]
            f = Excel(file_name)
            f.openSheet(file_name)
            array = f.readAllRows()
            arr = modifi_match(array)
            all_data.append(arr)
    return all_data

'''
    Cosa importiamo
    datas = import_data()
    datas --> len = 5; type = list
    datas[0] = Bundesliga --- datas[1] = LaLiga --- datas[2] = Ligue 1 --- datas[3] = Premier League --- datas[4] = Serie A
    datas[x][0] --> match per campionato x
    datas[x][y][n] --> elemento del match
    n = ...
        0 --> data
        1 --> team casa
        2 --> team ospite
        3 --> posizione classifica team casa
        4 --> posizione classifica team ospite
        5 --> punti nelle ultime 10 casa
        6 --> punti nelle ultime 10 ospiti
        7 --> goal pt 1 --> OUTPUT
        8 --> goal pt 2 --> OUTPUT
        9 --> goal st 1 --> OUTPUT
        10 --> goal st 2 --> OUTPUT
        11 --> goal tot 1 --> OUTPUT
        12 --> goal tot 2 --> OUTPUT
        13 --> goal tot match --> OUTPUT
        14 --> poss palla 1
        15 --> poss palla 2
        16 --> tiri 1
        17 --> tiri 2
        18 --> tiri porta 1
        19 --> tiri porta 2
        20 --> tiri fuori 1
        21 --> tiri fuori 2
        22 --> tiri fermati 1
        23 --> tiri fermati 2
        24 --> punizioni 1
        25 --> punizioni 2
        26 --> angol1 1
        27 --> angoli 2
        28 --> fuorigioco 1
        29 --> fuorigioco 2
        30 --> parate 1
        31 --> parate 2
        32 --> falli 1
        33 --> falli 2
        34 --> rossi 1
        35 --> rossi 2
        36 --> gialli 1
        37 --> gialli 2
        38 --> passaggi 1
        39 --> passaggi 2
        40 --> contrasti 1
        41 --> contrasti 2
        42 --> Attacchi 1
        43 --> Attacchi 2
        44 --> attacchi pericolosi 1
        45 --> attacchi pericolosi 2
        46 --> infortunati 1
        47 --> infortunati 2
        48 --> quota 1
        49 --> quota x
        50 --> quota 2
        51 --> numero di over .5 1
        52 --> numero di over .5 2
        53 --> numero di under .5 1
        54 --> numero di under .5 2
        55 --> numero di over 1.5 1
        56 --> numero di over 1.5 2
        57 --> numero di under 1.5 1
        58 --> numero di under 1.5 2
        59 --> numero di over 2.5 1
        60 --> numero di over 2.5 2
        61 --> numero di under 2.5 1
        62 --> numero di under 2.5 2
        63 --> numero di over 3.5 1
        64 --> numero di over 3.5 2
        65 --> numero di under 3.5 1
        66 --> numero di under 3.5 2
        67 --> numero di over 4.5 1
        68 --> numero di over 4.5 2
        69 --> numero di under 4.5 1
        70 --> numero di under 4.5 2
        71 --> quota under .5 --> NON USABILE
        72 --> quota over .5 --> NON USABILE
        73 --> quota under 1.5
        74 --> quota over 1.5
        75 --> quota under 2.5
        76 --> quota over 2.5
        77 --> quota under 3.5
        78 --> quota over 3.5
        79 --> quota under 4.5
        80 --> quota over 4.5
        81 --> quota 12
        82 --> quota 1x
        83 --> quota x2
        84 --> quota GG
        85 --> quota NG
        86 --> % vittoria ultime partite 1
        87 --> % pareggi ultime partite 1
        88 --> % sconfitte ultime partite 1
        89 --> % over ultime partite 1
        90 --> % under ultime partite 1
        91 --> % vittoria ultime partite 2
        92 --> % pareggi ultime partite 2
        93 --> % sconfitte ultime partite 2
        94 --> % over ultime partite 2
        95 --> % under ultime partite 2
        96 --> % vittoria ultime partite 1 vs 2
        97 --> % pareggi ultime partite 1 vs 2
        98 --> % sconfitte ultime partite 1 vs 2
        99 --> % over ultime partite 1 vs 2
        100 --> % under ultime partite 1 vs 2
        101 --> % vittoria ultime partite in casa 1
        102 --> % pareggi ultime partite in casa 1
        103 --> % sconfitte ultime partite in casa 1
        104 --> % over ultime partite in casa 1
        105 --> % under ultime partite in casa 1
        106 --> % vittoria ultime partite in trasferta 2
        107 --> % pareggi ultime partite in trasferta 2
        108 --> % sconfitte ultime partite in trasferta 2
        109 --> % over ultime partite in trasferta 2
        110 --> % under ultime partite in trasferta 2
'''

class Data:
    """
    Def of a class = Data() -> List of Data for db
    """
    def __init__(self, name):
        self.imported_data = import_data()
        self.input = []  # feature
        self.output = []  # label
        self.name = self.cvs_name(name)

    def generate_input_output(self):
        """
        Def of a method = def generate_input_output(self) -> None
        Elimina i falsi valori dagli excel, tutti quelli che non possono essere utilizzati
        :return: input ed output (goalpt goal_tot esito)
        """
        for league in self.imported_data:
            for match in league:
                match_input = []
                match_output = []
                goalpt = 0
                goaltot = 0
                esito = 0
                for element in range(len(match)):
                    if element in [7, 8]:
                        goalpt += int(match[element])
                        '''Se si vogliono utilizzare i passaggi togliere 38 e 39 --> Si perdono i campionati vecchi'''
                        '''Se si vogliono utilizzare i tiri fermati togliere 22 e 23 --> Si perde tutta la bundesliga'''
                        '''Se si vogliono utilizzare i contrasti togliere 40,41 --> Si perde un po' di tutto'''
                    elif element in [9, 10, 71, 72, 40, 41, 38, 39, 22, 23]:
                        pass
                    elif element in [11, 12]:
                        if int(match[11]) > int(match[12]):
                            esito = 1
                        elif int(match[11]) < int(match[12]):
                            esito = 2
                        else:
                            esito = 'X'
                    elif element == 13:
                        goaltot += int(match[element])
                    else:
                        match_input.append(match[element])

                match_output.append(goalpt)
                match_output.append(goaltot)
                match_output.append(esito)

                self.input.append(match_input)
                self.output.append(match_output)

    def clean_data(self):
        """
        Def of a method = def clean_data(self) -> None
        Elimina le partite in cui un dato non è stato trattato correttamente
        :return: input ed output senza Not Found
        """
        for index, element in enumerate(self.input):
            if "Not Found" in element:
                self.input.pop(index)
                self.output.pop(index)

    def cvs_name(self, name):
        today = "_" + str(date.today()) + ".cvs"
        named = name + today
        return named

    def save_cvs(self):
        path = os.getcwd() + r"\csv"
        with open(os.path.join(path, self.name), 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for insert, inp in enumerate(self.input):
                row = []
                for new in self.output[insert]:
                    row.append(new)
                tot_row = inp + row
                writer.writerow(tot_row)

def main(name):
    d = Data(name)
    d.generate_input_output()
    d.clean_data()
    d.save_cvs()

if __name__ == "__main__":
    main("prova1")