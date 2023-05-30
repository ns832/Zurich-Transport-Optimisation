import openpyxl
import requests
import json
import numpy as np

#SQL postgres
import psycopg2
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'Webapp',
    password = open("password.txt").read() 
) 

#create corresponding SQL table
apikey = open("apikey.txt").read()  
cur = conn.cursor() 
cur.execute('DROP TABLE ZurichDist')
conn.commit()
cur.execute('CREATE TABLE ZurichDist (Stat_1 varchar(255), Stat_2 varchar(255), distance int)')
string = 'SELECT name FROM "zurich"'    
cur.execute(string)
conn.commit()
names = cur.fetchall()

i, j = 0, 0
for name in names:
    #create upper traingular matrix since all distances A->B == B->A
    for destination in names[i+1:]:
        location = name[0]
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + destination[0] + "&origins=" + location + "&units=metric&key=" + apikey
        payload, headers = {}, {}
        response = requests.request("GET", url, headers=headers, data=payload)
        y = json.loads(response.text)
        if y["rows"][0]["elements"][0]["status"] == "OK":
            print(location,destination[0])
            dist = y["rows"][0]["elements"][0]["distance"]["value"] 
            print(dist)
            if dist >= 5 and dist <= 2000: 
                cur.execute('INSERT INTO ZurichDist (Stat_1, Stat_2, distance ) VALUES ( \'' + str(location) + '\', \'' + str(destination[0]) + '\', ' + str(dist) +')')
                conn.commit()
    i += 1
    break