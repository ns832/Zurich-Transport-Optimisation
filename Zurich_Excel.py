import openpyxl
import requests
import json

database = dict()

#get corresponding bus stop names and IDs
wb = openpyxl.load_workbook(r"C:\Users\44774\Documents\Cambridge IIA\Advanced German\Zurich\Haltestellen - v2.xlsx")
sheet = wb.active
for row in range(2,759):
    ID = sheet['A' + str(row)].value
    name = sheet['C' + str(row)].value
    name = name.replace('Ã¼','ü')
    name = name.replace('Ã¶','ö')
    name = name.replace('Ã¤','ä')
    database[ID] = name

#get passenger data to corresponding stops
wb = openpyxl.load_workbook(r"C:\Users\44774\Documents\Cambridge IIA\Advanced German\Zurich\Reisen Pure Values.xlsx")
sheet = wb.active
for row in range(4,765):
    ID = sheet['J' + str(row)].value
    einsteiger = sheet['K' + str(row)].value
    aussteiger = sheet['L' + str(row)].value
    if einsteiger != '#DIV/0!' or aussteiger != '#DIV/0!':
        name = database.get(ID)
        if not name:
            print(ID)
            raise Exception
        database[ID] = (name, einsteiger,aussteiger)

#access Goggle Maps API and find latitudes, if two stops have the same latitudes then store in list
lat,duplicates = set(), set()
for key in database.keys():
    location = database.get(key)[0]     
    apikey = open("apikey.txt").read() 
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + location + "&inputtype=textquery&fields=geometry/location/lat&key=" + apikey
    payload, headers = {}, {}
    response = requests.request("GET", url, headers=headers, data=payload)
    y = json.loads(response.text)

    #add duplicate entries to a list, and add ones where a result doesn't appear
    if not y["candidates"]:
        duplicates.add(key)
        print('Not Found')
    else:
        coord = y["candidates"][0]["geometry"]["location"]["lat"]
        if coord in lat:
            duplicates.add(key)
            print('Duplicate')
        lat.add(coord)

#remove entries that google maps doesn't recognise (i.e. will just give 'Adliswil' instead of 'Adliswil, Ahornweg')
for key in duplicates:
    database.pop(key)
print(database)