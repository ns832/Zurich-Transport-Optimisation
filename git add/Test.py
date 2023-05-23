import openpyxl
import requests
import json
import psycopg2
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'Webapp',
    password = open("password.txt").read() 
)


apikey = open("apikey.txt").read() 
destination = "Cambridge"
location = "London"    
url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + destination + "&origins=" + location + "&units=metric&key=" + apikey
payload, headers = {}, {}
response = requests.request("GET", url, headers=headers, data=payload)
y = json.loads(response.text)
dist = y["rows"][0]["elements"][0]["distance"]["value"]
print(dist)