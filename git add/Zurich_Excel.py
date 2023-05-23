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


#create SQL table
cur = conn.cursor() 
cur.execute('DROP TABLE zurich')
conn.commit()
cur.execute('CREATE TABLE Zurich (name varchar(255), ID int, einsteiger int, aussteiger int)')
conn.commit()

#get corresponding bus stop names and IDs
wb = openpyxl.load_workbook(r"C:\Users\44774\Documents\Cambridge IIA\Advanced German\Zurich\Haltestellen - v2.xlsx")
sheet = wb.active
for row in range(2,759):
    ID = sheet['A' + str(row)].value
    name = sheet['C' + str(row)].value
    name = name.replace('Ã¼','ü')
    name = name.replace('Ã¶','ö')
    name = name.replace('Ã¤','ä')
    cur.execute('INSERT INTO Zurich (name, ID) VALUES ( \'' + name + '\', ' + str(ID) + ')')
    conn.commit()

#get passenger data to corresponding stops
wb = openpyxl.load_workbook(r"C:\Users\44774\Documents\Cambridge IIA\Advanced German\Zurich\Reisen Pure Values.xlsx")
sheet = wb.active
for row in range(4,765):
    ID = sheet['J' + str(row)].value
    einsteiger = sheet['K' + str(row)].value
    aussteiger = sheet['L' + str(row)].value
    if einsteiger != '#DIV/0!' and aussteiger != '#DIV/0!':
        cur.execute('SELECT (name) FROM Zurich WHERE ID = \'' + str(ID)  + '\'')
        conn.commit()
        name = cur.fetchone()[0]
        if not name:
            print(ID)
            raise Exception
        cur.execute('UPDATE Zurich SET einsteiger = ' + str(einsteiger) + ', aussteiger = ' + str(aussteiger)  + ' WHERE ID = \'' + str(ID)  + '\'')
        conn.commit()

#access Goggle Maps API and find latitudes, if two stops have the same latitudes then store in list
lat, duplicates = set(), set()
cur.execute('SELECT (name) FROM "zurich"' )
conn.commit()
names = cur.fetchall()
for name in names:
    location = name[0]     
    apikey = open("apikey.txt").read() 
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + location + "&inputtype=textquery&fields=geometry/location/lat&key=" + apikey
    payload, headers = {}, {}
    response = requests.request("GET", url, headers=headers, data=payload)
    y = json.loads(response.text)

    #add duplicate entries to a list, and add ones where a result doesn't appear
    if not y["candidates"]:
        duplicates.add(name[0])
        print('Not Found')
    else:
        coord = y["candidates"][0]["geometry"]["location"]["lat"]
        if coord in lat:
            duplicates.add(name[0])
            print('Duplicate')
        lat.add(coord)
    

#remove entries that google maps doesn't recognise (i.e. will just give 'Adliswil' instead of 'Adliswil, Ahornweg')
for name in duplicates:  
    cur.execute('DELETE FROM "zurich" WHERE name = ' + str(name))
    conn.commit()
    print(name, "has been deleted")


cur.execute('SELECT COUNT (name) FROM "ZurichData"'  )
conn.commit()
rows = cur.fetchone()[0]
i,j = 0,0
distance_matrix = np.zeros(rows,rows)
cur.execute('SELECT (name) FROM "zurich"' )
conn.commit()
names = cur.fetchall()
for name in names:
    #create upper traingular matrix since all distances A->B == B->A
    for destination in names[i:]:
        location = name    
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + destination[0] + "&origins=" + location[0] + "&units=metric&key=" + apikey
        payload, headers = {}, {}
        response = requests.request("GET", url, headers=headers, data=payload)
        y = json.loads(response.text)
        
        if y["rows"][0]["elements"][0]["status"] == "ok":
            dist = y["rows"][0]["elements"][0]["distance"]["value"]

        