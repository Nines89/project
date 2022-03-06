# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 16:50:23 2021

@author: Utente
"""
import re

def find_IDs(bodyElencoPartite):
    regex = r"(?P<ID>\w+)\" title=\"Clicca per i dettagli dell'incontro!\" "
    matches = re.finditer(regex, bodyElencoPartite, re.MULTILINE)
    return matches


class PageResult:
    def __init__(self, txt):
        self.data = None
        self.team1 = None
        self.classifica1 = None
        self.classifica2 = None
        self.team2 = None
        self.forma1 = None
        self.forma2 = None
        self.goalPT1 = None
        self.goalPT2 = None
        self.goalST1 = None
        self.goalST2 = None
        self.totGoal1 = None
        self.totGoal2 = None
        self.totGoal = None
        self.possPalla1 = None
        self.possPalla2 = None
        self.tiri1 = None
        self.tiri2 = None
        self.tiriPorta1 = None
        self.tiriPorta2 = None
        self.tiriFuori1 = None
        self.tiriFuori2 = None
        self.tiriFermati1 = None
        self.tiriFermati2 = None
        self.Punizioni1 = None
        self.Punizioni2 = None
        self.Angolo1 = None
        self.Angolo2 = None
        self.FuoriGioco1 = None
        self.FuoriGioco2 = None
        self.Parate1 = None
        self.Parate2 = None
        self.Falli1 = None
        self.Falli2 = None
        self.Rossi1 = None
        self.Rossi2 = None
        self.Gialli1 = None
        self.Gialli2 = None
        self.Passaggi1 = None
        self.Passaggi2 = None
        self.Contrasti1 = None
        self.Contrasti2 = None
        self.Attacchi1 = None
        self.Attacchi2 = None
        self.AttacchiPer1 = None
        self.AttacchiPer2 = None
        self.NumInfortunati1 = None
        self.NumInfortunati2 = None
        self.quota1 = None
        self.quotaX = None
        self.quota2 = None
        self.numOver05_1 = None
        self.numOver05_2 = None
        self.numUnder05_1 = None
        self.numUnder05_2 = None
        self.numOver15_1 = None
        self.numOver15_2 = None
        self.numUnder15_1 = None
        self.numUnder15_2 = None
        self.numOver25_1 = None
        self.numOver25_2 = None
        self.numUnder25_1 = None
        self.numUnder25_2 = None
        self.numOver35_1 = None
        self.numOver35_2 = None
        self.numUnder35_1 = None
        self.numUnder35_2 = None
        self.numOver45_1 = None
        self.numOver45_2 = None
        self.numUnder45_1 = None
        self.numUnder45_2 = None
        self.quotaUnd05 = None
        self.quotaOv05 = None
        self.quotaUnd15 = None
        self.quotaOv15 = None
        self.quotaUnd25 = None
        self.quotaOv25 = None
        self.quotaUnd35 = None
        self.quotaOv35 = None
        self.quotaUnd45 = None
        self.quotaOv45 = None
        self.quota12 = None
        self.quota1X = None
        self.quotaX2 = None
        self.quotaGG = None
        self.quotaNG = None
        self.lastMatchs1 = {"mat1": [0, 0, 0, 0], "mat2": [0, 0, 0, 0], "mat3": [0, 0, 0, 0], "mat4": [0, 0, 0, 0],
                            "mat5": [0, 0, 0, 0]}
        self.lastMatchs2 = {"mat1": [0, 0, 0, 0], "mat2": [0, 0, 0, 0], "mat3": [0, 0, 0, 0], "mat4": [0, 0, 0, 0],
                            "mat5": [0, 0, 0, 0]}
        self.prevMatchsVS = {"mat1": [0, 0, 0], "mat2": [0, 0, 0], "mat3": [0, 0, 0], "mat4": [0, 0, 0],
                             "mat5": [0, 0, 0]}
        self.lastMatchsCASA = {"mat1": [0, 0, 0, 0], "mat2": [0, 0, 0, 0], "mat3": [0, 0, 0, 0], "mat4": [0, 0, 0, 0],
                               "mat5": [0, 0, 0, 0]}
        self.lastMatchsTRASFERTA = {"mat1": [0, 0, 0, 0], "mat2": [0, 0, 0, 0], "mat3": [0, 0, 0, 0],
                                    "mat4": [0, 0, 0, 0], "mat5": [0, 0, 0, 0]}
        self.txt = txt

    def find_stat(self):
        def find_teams():
            allay = []
            regex = r"__overflow\">(?P<team>[\w \d]+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            for mat in matches:
                allay.append(mat.group("team"))
            self.team1 = allay[0]
            self.team2 = allay[1]

        def find_ToT_goal():
            regex = r"detailScore__wrapper\"\>[\s\S]+?>(?P<totGoal1>\d+)[\s\S]+?<span>(?P<totGoal2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.totGoal1 = matches.group("totGoal1")
            self.totGoal2 = matches.group("totGoal2")
            self.totGoal = str(int(self.totGoal1) + int(self.totGoal2))

        def possPalla():
            regex = r"stat__homeValue\"\>(?P<possPalla1>\d+).+Possesso Palla.+?stat__awayValue\"\>(?P<possPalla2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.possPalla1 = matches.group("possPalla1")
            self.possPalla2 = matches.group("possPalla2")

        def tiriTot():
            regex = r"stat__homeValue\"\>(?P<tiri1>\d+)\</div\>\<div class=\"stat__categoryName\">" \
                    r"Tiri\</div\>\<div class=\"stat__awayValue\"\>(?P<tiri2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.tiri1 = matches.group("tiri1")
            self.tiri2 = matches.group("tiri2")

        def tiriInPorta():
            regex = r"stat__homeValue\"\>(?P<tiriP1>\d+)\</div\>\<div " \
                    r"class=\"stat__categoryName\">Tiri in Porta\</div\>\<div class=\"stat__awayValue\"\>" \
                    r"(?P<tiriP2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.tiriPorta1 = matches.group("tiriP1")
            self.tiriPorta2 = matches.group("tiriP2")

        def tiriFuori():
            regex = r"stat__homeValue\"\>(?P<tiriFP1>\d+)\</div\>\<div class=\"stat__categoryName\">Tiri Fuori\</div\>\<div class=\"stat__awayValue\"\>(?P<tiriFP2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.tiriFuori1 = matches.group("tiriFP1")
            self.tiriFuori2 = matches.group("tiriFP2")

        def tiriFermati():
            regex = r"stat__homeValue\"\>(?P<tiriFF1>\d+)\</div\>\<div class=\"stat__categoryName\">Tiri Fermati\</div\>\<div class=\"stat__awayValue\"\>(?P<tiriFF2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.tiriFermati1 = matches.group("tiriFF1")
            self.tiriFermati2 = matches.group("tiriFF2")

        def Punizioni():
            regex = r"stat__homeValue\"\>(?P<pun1>\d+)\</div\>\<div class=\"stat_categoryName\">Punizioni\</div\>\<div class=\"stat__awayValue\"\>(?P<pun2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Punizioni1 = matches.group("pun1")
            self.Punizioni2 = matches.group("pun2")

        def Angoli():
            regex = r"stat__homeValue\"\>(?P<ang1>\d+)\</div\>\<div class=\"stat__categoryName\">Calci d'angolo\</div\>\<div class=\"stat__awayValue\"\>(?P<ang2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Angolo1 = matches.group("ang1")
            self.Angolo2 = matches.group("ang2")

        def Fuorigioco():
            regex = r"stat__homeValue\"\>(?P<fuor1>\d+)\</div\>\<div class=\"stat__categoryName\">Fuorigioco\</div\>\<div class=\"stat__awayValue\"\>(?P<fuor2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.FuoriGioco1 = matches.group("fuor1")
            self.FuoriGioco2 = matches.group("fuor2")

        def Parate():
            regex = r"stat__homeValue\"\>(?P<t1>\d+)\</div\>\<div class=\"stat__categoryName\">Parate\</div\>\<div class=\"stat__awayValue\"\>(?P<t2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Parate1 = matches.group("t1")
            self.Parate2 = matches.group("t2")

        def Falli():
            regex = r"stat__homeValue\"\>(?P<t1>\d+)\</div\>\<div class=\"stat__categoryName\">Falli\</div\>\<div class=\"stat__awayValue\"\>(?P<t2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Falli1 = matches.group("t1")
            self.Falli2 = matches.group("t2")

        def Rossi():
            regex = r"stat__homeValue\"\>(?P<t1>\d+)\</div\>\<div class=\"stat__categoryName\">Cartellini Rossi\</div\>\<div class=\"stat__awayValue\"\>(?P<t2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Rossi1 = matches.group("t1")
            self.Rossi2 = matches.group("t2")

        def Gialli():
            regex = r"stat__homeValue\"\>(?P<t1>\d+)\</div\>\<div class=\"stat__categoryName\">Cartellini Gialli\</div\>\<div class=\"stat__awayValue\"\>(?P<t2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Gialli1 = matches.group("t1")
            self.Gialli2 = matches.group("t2")

        def passComple():
            regex = r"stat__homeValue\"\>(?P<t1>\d+)\</div\>\<div class=\"stat_categoryName\">Passaggi Completati\</div\>\<div class=\"stat__awayValue\"\>(?P<t2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Passaggi1 = matches.group("t1")
            self.Passaggi2 = matches.group("t2")

        def Contrasti():
            regex = r"stat__homeValue\"\>(?P<t1>\d+)\</div\>\<div class=\"stat__categoryName\">Contrasti\</div\>\<div class=\"stat__awayValue\"\>(?P<t2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Contrasti1 = matches.group("t1")
            self.Contrasti2 = matches.group("t2")

        def Attacchi():
            regex = r"stat__homeValue\"\>(?P<t1>\d+)\</div\>\<div class=\"stat__categoryName\">Attacchi\</div\>\<div class=\"stat__awayValue\"\>(?P<t2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.Attacchi1 = matches.group("t1")
            self.Attacchi2 = matches.group("t2")

        def AttacchiPericolosi():
            regex = r"stat__homeValue\"\>(?P<t1>\d+)\</div\>\<div class=\"stat__categoryName\">Attacchi Pericolosi\</div\>\<div class=\"stat__awayValue\"\>(?P<t2>\d+)"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.AttacchiPer1 = matches.group("t1")
            self.AttacchiPer2 = matches.group("t2")

        def data_ora():
            regex = r"startTime[\s\S]+?>(?P<dataOra>\d{2}.\d{2}.\d{4} \d{2}:\d{2})"
            matches = re.search(regex, self.txt, re.MULTILINE)
            self.data = matches.group("dataOra")

        try:
            data_ora()
        except:
            self.data = "Not Found"

        try:
            AttacchiPericolosi()
        except:
            self.AttacchiPer1 = "Not Found"
            self.AttacchiPer2 = "Not Found"

        try:
            Attacchi()
        except:
            self.Attacchi1 = "Not Found"
            self.Attacchi2 = "Not Found"

        try:
            Contrasti()
        except:
            self.Contrasti1 = "Not Found"
            self.Contrasti2 = "Not Found"

        try:
            passComple()
        except:
            self.Passaggi1 = "Not Found"
            self.Passaggi2 = "Not Found"

        try:
            Gialli()
        except:
            self.Gialli1 = "0"
            self.Gialli2 = "0"

        try:
            Rossi()
        except:
            self.Rossi1 = "0"
            self.Rossi2 = "0"

        try:
            Falli()
        except:
            self.Falli1 = "Not Found"
            self.Falli2 = "Not Found"

        try:
            Parate()
        except:
            self.Parate1 = "Not Found"
            self.Parate2 = "Not Found"

        try:
            Fuorigioco()
        except:
            self.FuoriGioco1 = "Not Found"
            self.FuoriGioco2 = "Not Found"

        try:
            find_teams()
        except:
            self.team1 = "Not Found"
            self.team2 = "Not Found"

        try:
            find_ToT_goal()
        except:
            self.totGoal1 = "Not Found"
            self.totGoal2 = "Not Found"

        try:
            possPalla()
        except:
            self.possPalla1 = "Not Found"
            self.possPalla2 = "Not Found"

        try:
            tiriTot()
        except:
            self.tiri1 = "Not Found"
            self.tiri2 = "Not Found"

        try:
            tiriInPorta()
        except:
            self.tiriPorta1 = "Not Found"
            self.tiriPorta2 = "Not Found"

        try:
            tiriFuori()
        except:
            self.tiriFuori1 = "Not Found"
            self.tiriFuori2 = "Not Found"

        try:
            tiriFermati()
        except:
            self.tiriFermati1 = "Not Found"
            self.tiriFermati2 = "Not Found"

        try:
            Punizioni()
        except:
            self.Punizioni1 = "Not Found"
            self.Punizioni2 = "Not Found"

        try:
            Angoli()
        except:
            self.Angolo1 = "Not Found"
            self.Angolo2 = "Not Found"

    def find_infortunati(self):
        regex1 = r"lf__participant lf__scratchParticipant \""
        regex2 = r"lf__participant lf__scratchParticipant lf__isReversed"
        self.NumInfortunati1 = len(re.findall(regex1, self.txt, re.MULTILINE))
        self.NumInfortunati2 = len(re.findall(regex2, self.txt, re.MULTILINE))

    def find_ptResults(self):
        # regex = r"1 Tempo</div><div><span>(?P<pt1>\d+)</span> - <span>(?P<pt2>\d+)"
        regex = r"1 Tempo</div><div>(?P<pt1>\d+) - (?P<pt2>\d+)"
        matches = re.search(regex, self.txt, re.MULTILINE)
        self.goalPT1 = matches.group("pt1")
        self.goalPT2 = matches.group("pt2")

    def find_stResults(self):
        try:
            self.goalST1 = str(int(self.totGoal1) - int(self.goalPT1))
            self.goalST2 = str(int(self.totGoal2) - int(self.goalPT2))
        except:
            pass

    def find_quote_1x2(self):
        def q1x2():
            regex = r"ui-table__row[\s\S]+?(span class=\"\">)(?P<quote1>\d+.\d+)[\s\S]+?(span class=\"\">)" \
                    r"(?P<quoteX>\d+.\d+)[\s\S]+?(span class=\"\">)(?P<quote2>\d+.\d+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            sum1 = []
            sumX = []
            sum2 = []
            for mat in matches:
                sum1.append(float(mat.group("quote1")))
                sumX.append(float(mat.group("quoteX")))
                sum2.append(float(mat.group("quote2")))
            self.quota1 = round(sum(sum1) / len(sum1), 2)
            self.quotaX = round(sum(sumX) / len(sumX), 2)
            self.quota2 = round(sum(sum2) / len(sum2), 2)

        try:
            q1x2()
        except:
            self.quota1 = "Not Found"
            self.quotaX = "Not Found"
            self.quota2 = "Not Found"

    def find_quote_UO(self):
        def uo05():
            regex = r"oddsCell__noOddsCell\">0.5[\s\S]+?(<span class=\"\">)(?P<o05>\d+.\d+)[\s\S]+?(<span class=\"\">)(?P<u05>\d+.\d+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            sum_o05 = []
            sum_u05 = []
            for mat in matches:
                sum_o05.append(float(mat.group("o05")))
                sum_u05.append(float(mat.group("u05")))
            self.quotaOv05 = round(sum(sum_o05) / len(sum_o05), 2)
            self.quotaUnd05 = round(sum(sum_u05) / len(sum_u05), 2)

        def uo15():
            regex = r"oddsCell__noOddsCell\">1.5[\s\S]+?(<span class=\"\">)(?P<o15>\d+.\d+)[\s\S]+?(<span class=\"\">)(?P<u15>\d+.\d+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            sum_o15 = []
            sum_u15 = []
            for mat in matches:
                sum_o15.append(float(mat.group("o15")))
                sum_u15.append(float(mat.group("u15")))
            self.quotaOv15 = round(sum(sum_o15) / len(sum_o15), 2)
            self.quotaUnd15 = round(sum(sum_u15) / len(sum_u15), 2)

        def uo25():
            regex = r"oddsCell__noOddsCell\">2.5[\s\S]+?(<span class=\"\">)(?P<o25>\d+.\d+)[\s\S]+?(<span class=\"\">)(?P<u25>\d+.\d+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            sum_o25 = []
            sum_u25 = []
            for mat in matches:
                sum_o25.append(float(mat.group("o25")))
                sum_u25.append(float(mat.group("u25")))
            self.quotaOv25 = round(sum(sum_o25) / len(sum_o25), 2)
            self.quotaUnd25 = round(sum(sum_u25) / len(sum_u25), 2)

        def uo35():
            regex = r"oddsCell__noOddsCell\">3.5[\s\S]+?(<span class=\"\">)(?P<o35>\d+.\d+)[\s\S]+?(<span class=\"\">)(?P<u35>\d+.\d+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            sum_o35 = []
            sum_u35 = []
            for mat in matches:
                sum_o35.append(float(mat.group("o35")))
                sum_u35.append(float(mat.group("u35")))
            self.quotaOv35 = round(sum(sum_o35) / len(sum_o35), 2)
            self.quotaUnd35 = round(sum(sum_u35) / len(sum_u35), 2)

        def uo45():
            regex = r"oddsCell__noOddsCell\">4.5[\s\S]+?(<span class=\"\">)(?P<o45>\d+.\d+)[\s\S]+?(<span class=\"\">)(?P<u45>\d+.\d+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            sum_o45 = []
            sum_u45 = []
            for mat in matches:
                sum_o45.append(float(mat.group("o45")))
                sum_u45.append(float(mat.group("u45")))
            self.quotaOv45 = round(sum(sum_o45) / len(sum_o45), 2)
            self.quotaUnd45 = round(sum(sum_u45) / len(sum_u45), 2)

        try:
            uo45()
        except:
            self.quotaOv45 = "Not Found"
            self.quotaUnd45 = "Not Found"

        try:
            uo35()
        except:
            self.quotaOv35 = "Not Found"
            self.quotaUnd35 = "Not Found"

        try:
            uo25()
        except:
            self.quotaOv25 = "Not Found"
            self.quotaUnd25 = "Not Found"

        try:
            uo15()
        except:
            self.quotaOv15 = "Not Found"
            self.quotaUnd15 = "Not Found"

        try:
            uo05()
        except:
            self.quotaOv05 = "Not Found"
            self.quotaUnd05 = "Not Found"

    def find_quote_DC(self):
        def qDC():
            regex = r"(oddsCell__odd )[\s\S]+?(<span class=\"\">)(?P<dc>\d+.\d+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            sum1X = []
            sum12 = []
            sumX2 = []

            for res, mat in enumerate(matches):
                if res in [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]: sum1X.append(float(mat.group("dc")))
                if res in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]: sum12.append(float(mat.group("dc")))
                if res in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]: sumX2.append(float(mat.group("dc")))
            self.quota1X = round(sum(sum1X) / len(sum1X), 2)
            self.quota12 = round(sum(sum12) / len(sum12), 2)
            self.quotaX2 = round(sum(sumX2) / len(sumX2), 2)

        try:
            qDC()
        except:
            self.quota1X = "Not Found"
            self.quota12 = "Not Found"
            self.quotaX2 = "Not Found"

    def find_quote_GG(self):
        def gg():
            regex = r"oddsCell__odd [\s\S]+?(span class=\"\">)(?P<gg>\d+.\d+)"
            matches = re.finditer(regex, self.txt, re.MULTILINE)
            sumGG = []
            sumNG = []

            for res, mat in enumerate(matches):
                if res in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]: sumGG.append(float(mat.group("gg")))
                if res in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]: sumNG.append(float(mat.group("gg")))
            self.quotaGG = round(sum(sumGG) / len(sumGG), 2)
            self.quotaNG = round(sum(sumNG) / len(sumNG), 2)

        try:
            gg()
        except:
            self.quotaGG = "Not Found"
            self.quotaNG = "Not Found"

    def find_last_match(self):
        def changing(string):
            regex = r"(?P<f>\d+) : (?P<l>\d+)"
            subst = "\g<l> : \g<f>"
            result = re.sub(regex, subst, string, 0, re.MULTILINE)
            if result:
                return result

        def lm():
            regex = r"(?P<casa>h2h__homeParticipant[\s\S]+?)\"[\s\S]+?Inner " \
                    r"[\s\S]+?>(?P<team1>[\w\s]+)[\s\S]+?Inner [\s\S]+?>" \
                    r"(?P<team2>[\w\s]+)[\s\S]+?result\"><span>(?P<res1>\d+)" \
                    r"</span><span>(?P<res2>\d+)[\s\S]+?title=[\s\S]+?>(?P<final>\w)"

            matches = re.finditer(regex, self.txt, re.MULTILINE)
            control = sum(1 for m in re.finditer(regex, self.txt, re.MULTILINE))
            if control >= 10:
                inf = 0
                for count, mat in enumerate(matches):
                    result = str(mat.group("res1") + ' : ' + mat.group("res2"))
                    if count < 5:
                        inf += 1
                        if "h2h__participant highlighted" in mat.group("casa"):
                            self.lastMatchs1["mat" + str(inf)][0] = mat.group("team1")
                            self.lastMatchs1["mat" + str(inf)][1] = mat.group("team2")
                            self.lastMatchs1["mat" + str(inf)][2] = result
                            self.lastMatchs1["mat" + str(inf)][3] = mat.group("final")
                        else:
                            self.lastMatchs1["mat" + str(inf)][1] = mat.group("team1")
                            self.lastMatchs1["mat" + str(inf)][0] = mat.group("team2")
                            self.lastMatchs1["mat" + str(inf)][2] = changing(result)
                            self.lastMatchs1["mat" + str(inf)][3] = mat.group("final")

                    elif count < 10:
                        inf += 1
                        if "h2h__participant highlighted" in mat.group("casa"):
                            self.lastMatchs2["mat" + str(inf - 5)][0] = mat.group("team1")
                            self.lastMatchs2["mat" + str(inf - 5)][1] = mat.group("team2")
                            self.lastMatchs2["mat" + str(inf - 5)][2] = result
                            self.lastMatchs2["mat" + str(inf - 5)][3] = mat.group("final")
                        else:
                            self.lastMatchs2["mat" + str(inf - 5)][1] = mat.group("team1")
                            self.lastMatchs2["mat" + str(inf - 5)][0] = mat.group("team2")
                            self.lastMatchs2["mat" + str(inf - 5)][2] = changing(result)
                            self.lastMatchs2["mat" + str(inf - 5)][3] = mat.group("final")
                    elif count >= 10:
                        inf += 1
                        self.prevMatchsVS["mat" + str(inf - 10)][0] = mat.group("team1")
                        self.prevMatchsVS["mat" + str(inf - 10)][1] = mat.group("team2")
                        self.prevMatchsVS["mat" + str(inf - 10)][2] = result

        try:
            lm()
        except:
            self.lastMatchs1 = "Not Found"
            self.lastMatchs2 = "Not Found"
            self.prevMatchsVS = "Not Found"

    def lm_CASA_match(self):
        def lmCASA():
            regex = r"(h2h__homeParticipant h2h__participant highlighted)\"[\s\S]+?(Inner [\s\S]+?>)" \
                    r"(?P<team1>[\w\s]+)[\s\S]+?" \
                    r"(Inner [\s\S]+?>)(?P<team2>[\w\s]+)[\s\S]+?result\"><span>(?P<res1>\d+)</span><span>" \
                    r"(?P<res2>\d+)[\s\S]+?" \
                    r"title=[\s\S]+?>(?P<final>\w)"

            matches = re.finditer(regex, self.txt, re.MULTILINE)
            inf = 0
            for count, mat in enumerate(matches):
                inf += 1
                result = str(mat.group("res1") + ' : ' + mat.group("res2"))
                self.lastMatchsCASA["mat" + str(inf)][0] = mat.group("team1")
                self.lastMatchsCASA["mat" + str(inf)][1] = mat.group("team2")
                self.lastMatchsCASA["mat" + str(inf)][2] = result
                self.lastMatchsCASA["mat" + str(inf)][3] = mat.group("final")

        try:
            lmCASA()
        except:
            self.lastMatchsCASA = "Not Found"


    def lm_TRANSFERTA_match(self):
        def lmTRANSFERTA():

            regex = r"(h2h__homeParticipant h2h__participant )\"[\s\S]+?(Inner [\s\S]+?>)" \
                    r"(?P<team1>[\w\s]+)[\s\S]+?" \
                    r"(Inner [\s\S]+?>)(?P<team2>[\w\s]+)[\s\S]+?result\"><span>(?P<res1>\d+)</span><span>" \
                    r"(?P<res2>\d+)[\s\S]+?" \
                    r"title=[\s\S]+?>(?P<final>\w)"

            matches = re.finditer(regex, self.txt, re.MULTILINE)
            inf = 0
            for count, mat in enumerate(matches):
                if count < 5:
                    inf += 1
                    result = str(mat.group("res1") + ' : ' + mat.group("res2"))
                    self.lastMatchsTRASFERTA["mat" + str(inf)][0] = mat.group("team1")
                    self.lastMatchsTRASFERTA["mat" + str(inf)][1] = mat.group("team2")
                    self.lastMatchsTRASFERTA["mat" + str(inf)][2] = result
                    self.lastMatchsTRASFERTA["mat" + str(inf)][3] = mat.group("final")


        try:
            lmTRANSFERTA()
        except:
            self.lastMatchsTRASFERTA = "Not Found"

    def find_classifica(self):
        regex = r";\">(?P<pos1>\d+).[\s\S]+?tableCellParticipant__name\">(?P<team1>\w+)" \
                r"|title=\"\">(?P<pos2>\d+).[\s\S]+?tableCellParticipant__name\">(?P<team2>\w+)"
        matches = re.finditer(regex, self.txt, re.MULTILINE)
        for mat in matches:
            if mat.group("pos1") is not None:
                if mat.group("team1") == self.team1:
                    self.classifica1 = mat.group("pos1")
                elif mat.group("team1") == self.team2:
                    self.classifica2 = mat.group("pos1")
            else:
                if mat.group("team2") == self.team1:
                    self.classifica1 = mat.group("pos2")
                elif mat.group("team2") == self.team2:
                    self.classifica2 = mat.group("pos2")

    def find_forma(self):
        regex = r"title=\"\">(?P<pos>\d+).[\s\S]+?tableCellParticipant__name\">(?P<team>\w+)" \
                r"[\s\S]+?points \">(?P<forma>\d+)"
        matches = re.finditer(regex, self.txt, re.MULTILINE)
        for mat in matches:
            if mat.group("team") == self.team1:
                self.forma1 = mat.group("forma")
            elif mat.group("team") == self.team2:
                self.forma2 = mat.group("forma")

    def n_Over_Under_05(self):
        regex = r"ui-table__row table__row--selected [\s\S]+?_name\">(?P<team>\w+)" \
                r"[\s\S]+?over \">(?P<over>\d+)[\s\S]+?under \">(?P<under>\d+)"
        matches = re.finditer(regex, self.txt, re.MULTILINE)
        for mat in matches:
            if mat.group("team") == self.team1:
                self.numUnder05_1 = mat.group("under")
                self.numOver05_1 = mat.group("over")
            elif mat.group("team") == self.team2:
                self.numUnder05_2 = mat.group("under")
                self.numOver05_2 = mat.group("over")

    def n_Over_Under_15(self):
        regex = r"ui-table__row table__row--selected [\s\S]+?_name\">(?P<team>\w+)" \
                r"[\s\S]+?over \">(?P<over>\d+)[\s\S]+?under \">(?P<under>\d+)"
        matches = re.finditer(regex, self.txt, re.MULTILINE)
        for mat in matches:
            if mat.group("team") == self.team1:
                self.numUnder15_1 = mat.group("under")
                self.numOver15_1 = mat.group("over")
            elif mat.group("team") == self.team2:
                self.numUnder15_2 = mat.group("under")
                self.numOver15_2 = mat.group("over")

    def n_Over_Under_25(self):
        regex = r"ui-table__row table__row--selected [\s\S]+?_name\">(?P<team>\w+)" \
                r"[\s\S]+?over \">(?P<over>\d+)[\s\S]+?under \">(?P<under>\d+)"
        matches = re.finditer(regex, self.txt, re.MULTILINE)
        for mat in matches:
            if mat.group("team") == self.team1:
                self.numUnder25_1 = mat.group("under")
                self.numOver25_1 = mat.group("over")
            elif mat.group("team") == self.team2:
                self.numUnder25_2 = mat.group("under")
                self.numOver25_2 = mat.group("over")

    def n_Over_Under_35(self):
        regex = r"ui-table__row table__row--selected [\s\S]+?_name\">(?P<team>\w+)" \
                r"[\s\S]+?over \">(?P<over>\d+)[\s\S]+?under \">(?P<under>\d+)"
        matches = re.finditer(regex, self.txt, re.MULTILINE)
        for mat in matches:
            if mat.group("team") == self.team1:
                self.numUnder35_1 = mat.group("under")
                self.numOver35_1 = mat.group("over")
            elif mat.group("team") == self.team2:
                self.numUnder35_2 = mat.group("under")
                self.numOver35_2 = mat.group("over")

    def n_Over_Under_45(self):
        regex = r"ui-table__row table__row--selected [\s\S]+?_name\">(?P<team>\w+)" \
                r"[\s\S]+?over \">(?P<over>\d+)[\s\S]+?under \">(?P<under>\d+)"
        matches = re.finditer(regex, self.txt, re.MULTILINE)
        for mat in matches:
            if mat.group("team") == self.team1:
                self.numUnder45_1 = mat.group("under")
                self.numOver45_1 = mat.group("over")
            elif mat.group("team") == self.team2:
                self.numUnder45_2 = mat.group("under")
                self.numOver45_2 = mat.group("over")

def checkNormalMatch(txt):
    regex = r"<span class=\"tournamentHeader__country\">\w+: <a href=\"[\s\S]+? - (?P<days>\w+)"
    matches = re.search(regex, txt, re.MULTILINE)
    if matches:
        return matches.group("days")
    else:
        return False

if __name__ == "__main__":
    with open("demo.txt", "r", encoding="utf8") as f:
        txt = f.read()

    p = PageResult(txt)
    p.find_stat()
    print(p.Contrasti1)
    print(p.Contrasti2)


