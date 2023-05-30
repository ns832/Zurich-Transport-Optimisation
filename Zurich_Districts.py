import openpyxl
import requests
import json
import numpy as np


districts = set()
#SQL postgres
import psycopg2
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'Webapp',
    password = open("password.txt").read() 
) 
cur = conn.cursor() 
string = 'SELECT name FROM "zurich"'    
cur.execute(string)
conn.commit()
names = cur.fetchall()
for name in names:
    all_words = name[0]
    split = all_words.split()[0]
    extracted_string = ''.join(filter(str.isalnum, split))
    districts.add(extracted_string)
print(districts)

string = 'SELECT * FROM "zurich" ORDER by name ASC'    
cur.execute(string)
conn.commit()
names = cur.fetchall()
closest_stations = dict()
i=0
Adliswil = list(range(22))
Aesch = list(range(22,24))
Benglen = list(range(24,27))
Bergdieton = list(range(25,34))
Binz = list(range(34,38))
Birmensdorf = list(range(38,44))
Dietikon = list(range(44,71))
Dübensdorf = list(range(71,82))
Ebmatingen = list(range(82,85))
Effretikon = 85
Egg = 86
Emmat = 87
Esslingen = 88
Fahrweid = list(range(89,92))
Fällanden = list(range(92,101))
Forch = [101,102]
Geroldswil = list(range(103,108))
Glanzenberg = 108
Glattbrugg = list(range(109,116))
Glattpark = list(range(116,121))
Gockhausen = [121,122]
Hinteregg = 123
Itschnach = list(range(124,128))
Kilchberg = list(range(128,152))
Killwangen = 152
Kindhausen = [153,154]
Kloten = list(range(155,161))
Küsnacht = list(range(161,180))
Langwies = 180
Maiacher = 181
Maur = list(range(182,187))
Neue = 187
Neuhaus = 188
Oberengstringen = list(range(189,193))
Oetwil = list(range(193,197))
Opfikon = [197,198]
Pfaffhausen = list(range(199,203))
Rümlang = 203
Rüschlikon = list(range(204,216))
Scheuren = [216,217]
Schlieren = list(range(218,239))
Schwerzenbach = [239,240]
Spital = 241
Spreitenbach = list(range(242,251))
Thalwil = list(range(251,257))
Uitikon = 257
Unterengstringen = list(range(258,264))
Urdorf = list(range(264,278))
Volketswil = [278,279]
Wädenswil = 280
Waldburg = [281,282]
Waldegg = [283,284,285]
Wallisellen = list(range(286,292))
Waltikon = 292
Weiningen = list(range(293,297))
Zch = 297
Zollikerb = 298
Zollikerberg = list(range(299,306))
Zollikon = list(range(306,319))
Zumikon = list(range(319,323))
Zürich = list(range(323,758))

for i in range(len(names)):
    if i < 20:#adliswil
    if i >= 299 and i <= 304:#zollikerberg
        #zollikon, waltikon, maiacher, ebmatingen, pfaffhausen, gockhausen, kusnacht
        closest_stations[i] = [306,318]

#urdorf - Bergdietikon, killwangen, glattpark, birmensdorf, geroldswil, Unterengstringen, Fahrweid, glanzenberg, spreitenbach, Zürich,Kalkbreite/Bhf.Wiedikon, uitikon, oberengstringen, weiningen, oetwil, schlieren, aesch, kindhausen