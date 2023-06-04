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
# string = 'SELECT name FROM "zurich"'    
# cur.execute(string)
# conn.commit()
# names = cur.fetchall()
# for name in names:
#     all_words = name[0]
#     split = all_words.split()[0]
#     extracted_string = ''.join(filter(str.isalnum, split))
#     districts.add(extracted_string)
# print(districts)

# string = 'SELECT * FROM "zurich" ORDER by name ASC'    
# cur.execute(string)
# conn.commit()
# names = cur.fetchall()
closest_stations = dict()

Adliswil = list(range(1,22))
Aesch = list(range(22,24))
Benglen = [24, 25]
Bergdietikon = list(range(27,34))
Binz = list(range(34,38))
Birmensdorf = list(range(38,44))
Dietikon = list(range(44,71))
Dübensdorf = list(range(71,82))
Ebmatingen = list(range(82,85))
Effretikon = [85]
Egg = [86]
Emmat = [87]
Esslingen = [88]
Fahrweid = list(range(89,92))
Fällanden = list(range(92,101))
Forch = [101,102]
Geroldswil = list(range(103,108))
Glanzenberg = [108]
Glattbrugg = list(range(109,116))
Glattpark = list(range(116,121))
Gockhausen = [121,122]
Hinteregg = [123]
Itschnach = list(range(124,128))
Kilchberg = list(range(128,152))
Killwangen = [152]
Kindhausen = [153,154]
Kloten = list(range(155,161))
Küsnacht = list(range(161,180))
Langwies = [180]
Maiacher = [181]
Maur = list(range(182,187))
Neue = [187]
Neuhaus = [188]
Oberengstringen = list(range(189,193))
Oetwil = list(range(193,197))
Opfikon = [197,198]
Pfaffhausen = list(range(199,203))
Rümlang = [203]
Rüschlikon = list(range(204,216))
Scheuren = [216,217]
Schlieren = list(range(218,239))
Schwerzenbach = [239,240]
Spital = [241]
Spreitenbach = list(range(242,251))
Thalwil = list(range(251,257))
Uitikon = [257]
Unterengstringen = list(range(258,264))
Urdorf = list(range(264,278))
Volketswil = [278,279]
Wädenswil = [280]
Waldburg = [281,282]
Waldegg = [283,284,285]
Wallisellen = list(range(286,292))
Waltikon = [292]
Weiningen = list(range(293,297))
Zch = [297]
Zollikerb = [298]
Zollikerberg = list(range(299,306))
Zollikon = list(range(306,319))
Zumikon = list(range(319,323))
# Zürich = list(range(323,758))
Zürich = list(range(456,758))

apikey = open("apikey.txt").read() 
closest_stations['Adliswil'] = Adliswil + Aesch + Zürich + Zch + Birmensdorf
# for i in Adliswil:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Adliswil']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                     string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                     cur.execute(string)
#                     conn.commit()
# raise Exception

#closest_stations['Aesch'] = Aesch  + Birmensdorf + Waldegg + Kilchberg + Urdorf # + Adliswil

closest_stations['Benglen'] = Benglen + Fällanden + Pfaffhausen + Binz + Ebmatingen + Maur
# for i in Benglen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Benglen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Bergdietikon'] = Bergdietikon + Spreitenbach + Dietikon + Fahrweid + Glanzenberg + Urdorf + Schlieren + Uitikon # + Birmensdorf
# for i in Bergdietikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Bergdietikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Binz'] = Binz + Pfaffhausen + Ebmatingen + Zollikerb + Zollikerberg + Spital + Waltikon # + Benglen
# for i in Binz:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Binz']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Birmensdorf'] = Birmensdorf + Uitikon + Waldegg + Urdorf + Kilchberg # + Adliswil + Aesch + Bergdietikon
# for i in Birmensdorf:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Birmensdorf']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Dietikon'] = Dietikon + Spreitenbach + Geroldswil + Fahrweid + Weiningen + Glanzenberg + Urdorf # + Bergdietikon 
# for i in Dietikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Dietikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Dübensdorf'] = Dübensdorf + Wallisellen + Gockhausen + Kindhausen + Volketswil + Schwerzenbach + Fällanden + Pfaffhausen
# for i in Dübensdorf:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Dübensdorf']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Ebmatingen'] = Ebmatingen + Maur + Waltikon + Zumikon + Maiacher + Neue + Forch # + Binz + Benglen
# for i in Ebmatingen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Ebmatingen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Effretikon'] = Effretikon + Kindhausen + Volketswil
# for i in Effretikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Effretikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Egg'] = Egg + Esslingen + Langwies + Hinteregg
# for i in Egg:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Egg']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Emmat'] = Emmat + Esslingen + Langwies
# for i in Emmat:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Emmat']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Esslingen'] = Esslingen + Langwies + Oetwil
# for i in Esslingen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Esslingen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Fahrweid'] = Fahrweid + Geroldswil + Weiningen + Glanzenberg + Unterengstringen + Schlieren # + Dietikon
# for i in Fahrweid:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Fahrweid']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Fällanden'] = Fällanden + Schwerzenbach + Pfaffhausen # + Dübensdorf + Benglen
# for i in Fällanden:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Fällanden']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Forch'] = Forch + Neue + Scheuren + Maur # + Ebmatingen
# for i in Forch:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Forch']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Geroldswil'] = Geroldswil + Weiningen + Spreitenbach #  + Fahrweid
# for i in Geroldswil:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Geroldswil']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Glanzenberg'] = Glanzenberg + Schlieren + Urdorf # + Bergdietikon + Fahrweid + Dietikon
# for i in Glanzenberg:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Glanzenberg']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Glattbrugg'] = Glattbrugg + Opfikon + Wallisellen + Kloten + Glattpark
# for i in Glattbrugg:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Glattbrugg']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Glattpark'] = Glattpark + Opfikon + Wallisellen # + Glattbrugg
# for i in Glattpark:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Glattpark']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Gockhausen'] = Gockhausen + Pfaffhausen # + Dübensdorf 
# for i in Gockhausen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Gockhausen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Hinteregg'] = Hinteregg + Scheuren # + Egg
# for i in Hinteregg:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Hinteregg']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Itschnach'] = Itschnach + Küsnacht + Zollikon + Zumikon + Waltikon
# for i in Itschnach:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Itschnach']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Kilchberg'] = Kilchberg + Rüschlikon # + Adliswil
# for i in Kilchberg:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Kilchberg']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Killwangen'] = Killwangen + Spreitenbach
# for i in Killwangen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Killwangen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Kindhausen'] = Kindhausen + Volketswil + Schwerzenbach # + Effretikon
# for i in Kindhausen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Kindhausen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Kloten'] = Kloten + Opfikon + Rümlang
# for i in Kloten:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Kloten']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Küsnacht'] = Küsnacht + Zollikon # + Itschnach
# for i in Küsnacht:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Küsnacht']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Langwies'] = Langwies # + Egg + Esslingen
# for i in Langwies:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Langwies']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Maiacher'] = Maiacher + Maur + Zumikon + Waltikon + Neue # + Ebmatingen
# for i in Maiacher:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Maiacher']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Maur'] = Maur + Neue + Scheuren # + Ebmatingen + Forch + Maiacher
# for i in Maur:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Maur']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Neue'] = Neue + Scheuren # + Maur + Maiacher + Forch 
# for i in Neue:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Neue']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Oberengstringen'] = Oberengstringen + Unterengstringen + Schlieren
# for i in Oberengstringen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Oberengstringen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Oetwil'] = Oetwil # + Esslingen
# for i in Oetwil:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Oetwil']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Opfikon'] = Opfikon # + Glattpark + Kloten
# for i in Opfikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Opfikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Pfaffhausen'] = Pfaffhausen # + Benglen + Binz + Fällanden + Gockhausen
# for i in Pfaffhausen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Pfaffhausen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Rümlang'] = Rümlang # + Kloten + Opfikon
# for i in Rümlang:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Rümlang']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Rüschlikon'] = Rüschlikon + Thalwil # + Kilchberg + Adliswil
# for i in Rüschlikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Rüschlikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Scheuren'] = Scheuren # + Forch + Hinteregg
# for i in Scheuren:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Scheuren']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Schlieren'] = Schlieren + Urdorf + Unterengstringen # + Glanzenberg + Fahrweid + Oberengstringen
# for i in Schlieren:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Schlieren']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Schwerzenbach'] = Schwerzenbach + Volketswil # + Fällanden + Dübensdorf
# for i in Schwerzenbach:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Schwerzenbach']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Spital'] = Spital + Zollikerb + Waldburg
# for i in Spital:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Spital']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Spreitenbach'] = Spreitenbach # + Killwangen + Geroldswil
# for i in Spreitenbach:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Spreitenbach']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Thalwil'] = Thalwil # + Rüschlikon
# for i in Thalwil:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Thalwil']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Uitikon'] = Uitikon + Waldegg + Urdorf # + Birmensdorf
# for i in Uitikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Uitikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Unterengstringen'] = Unterengstringen + Weiningen # + Oberengstringen
# for i in Unterengstringen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Unterengstringen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Urdorf'] = Urdorf # + Glanzenberg + Bergdietikon + Uitikon + Schlieren
# for i in Urdorf:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Urdorf']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Volketswil'] = Volketswil # + Schwerzenbach + Kindhausen
# for i in Volketswil:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Volketswil']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Wädenswil'] = Wädenswil # + Thalwil
# for i in Wädenswil:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Wädenswil']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Waldburg'] = Waldburg + Zollikerb + Zollikerberg + Zollikon
# for i in Waldburg:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Waldburg']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Waldegg'] = Waldegg # + Birmensdorf
# for i in Waldegg:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Waldegg']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Wallisellen'] = Wallisellen # + Glattpark + Dübensdorf
# for i in Wallisellen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Wallisellen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Waltikon'] = Waltikon + Zumikon + Zollikerberg # + Itschnach + Maiacher
# for i in Waltikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Waltikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Weiningen'] = Weiningen # + Unterengstringen + Fahrweid + Geroldswil
# for i in Weiningen:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Weiningen']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Zch'] = Zch + Zürich
# for i in Zch:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Zch']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Zollikerb'] = Zollikerb + Zollikerberg # + Spital + Waldburg + Waltikon
# for i in Zollikerb:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Zollikerb']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Zollikerberg'] = Zollikerberg # + Spital + Waldburg + Waltikon + Zollikerb
# for i in Zollikerberg:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Zollikerberg']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Zollikon'] = Zollikon # + Waldburg + Itschnach
# for i in Zollikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Zollikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Zumikon'] = Zumikon # + Maiacher + Waltikon + Itschnach + Neue
# for i in Zumikon:
#     string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
#     cur.execute(string)
#     conn.commit()
#     name = cur.fetchall()
#     if name is not [] and len(name) != 0:
#         name_i = name[0][0]
#         for j in closest_stations['Zumikon']:
#             if i is not j:
#                 string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
#                 cur.execute(string)
#                 conn.commit()
#                 name = cur.fetchall()
#                 if name is not [] and len(name) != 0:
#                     name_j = name[0][0]
#                     url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
#                     payload, headers = {}, {}
#                     response = requests.request("GET", url, headers=headers, data=payload)
#                     y = json.loads(response.text)
#                     if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
#                         print(name_i, name_j)
#                         dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
#                         string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
#                         cur.execute(string)
#                         conn.commit()
# raise Exception
closest_stations['Zürich'] = Zürich # + Zollikon + Wallisellen + Schlieren
for i in Zürich:
    string = 'SELECT name FROM "zurich" WHERE key = {}'.format(i)
    cur.execute(string)
    conn.commit()
    name = cur.fetchall()
    if name is not [] and len(name) != 0:
        name_i = name[0][0]
        for j in closest_stations['Zürich']:
            if i is not j:
                string = 'SELECT name FROM "zurich" WHERE key = {}'.format(j)
                cur.execute(string)
                conn.commit()
                name = cur.fetchall()
                if name is not [] and len(name) != 0:
                    name_j = name[0][0]
                    url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + name_j + "&origins=" + name_i + "&units=metric&key=" + apikey
                    payload, headers = {}, {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    y = json.loads(response.text)
                    print(y)
                    if y["destination_addresses"] != [''] and y["origin_addresses"] != ['']:
                        print(name_i, name_j)
                        dist = str(y["rows"][0]["elements"][0]["distance"]["value"])
                        string = 'INSERT INTO "zurichdist" (stat_1, stat_2, distance) VALUES ( \'' + name_j + '\', \'' + name_i  + '\', ' + dist + ')'
                        cur.execute(string)
                        conn.commit()
raise Exception

print("Amount of entries", len(closest_stations['Zch']))
# cur.execute('SELECT (name) FROM "zurich"' )
# conn.commit()
# names = cur.fetchall()
# for name in names:
for number in range(757):
    cur.execute('SELECT (name) FROM "zurich" WHERE id = ')
    conn.commit()
    names = cur.fetchone()
#     #create upper traingular matrix since all distances A->B == B->A
#     for destination in names[i:]:
#         location = name    
#         url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + destination[0] + "&origins=" + location[0] + "&units=metric&key=" + apikey
#         payload, headers = {}, {}
#         response = requests.request("GET", url, headers=headers, data=payload)
#         y = json.loads(response.text)
        
#         if y["rows"][0]["elements"][0]["status"] == "ok":
#             dist = y["rows"][0]["elements"][0]["distance"]["value"]