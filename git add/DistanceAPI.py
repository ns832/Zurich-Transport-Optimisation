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

apikey = open("apikey.txt").read()  
cur = conn.cursor() 
string = 'SELECT COUNT (name) FROM "ZurichData"'    
cur.execute(string)
conn.commit()
rows = cur.fetchone()[0]

#create empty square matrix of size equal to the number of bus stops
distance_matrix = np.empty([rows,rows])
string = 'SELECT name FROM "ZurichData"'    
cur.execute(string)
conn.commit()
names = cur.fetchall()

i = 0
j = 0
for name in names:
    #create upper traingular matrix since all distances A->B == B->A
    for destination in names[i:]:
        location = name[0]
        print(location)
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + destination[0] + "&origins=" + location + "&units=metric&key=" + apikey
        payload, headers = {}, {}
        response = requests.request("GET", url, headers=headers, data=payload)
        y = json.loads(response.text)
        print(y)
        if y["rows"][0]["elements"][0]["status"] == "ok":
            dist = y["rows"][0]["elements"][0]["distance"]["value"] 
            distance_matrix[i,j] = distance_matrix[j,i] = dist
        i += 1
        print(distance_matrix[i,j])
    j += 1