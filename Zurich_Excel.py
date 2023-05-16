import openpyxl

database = dict()

wb = openpyxl.load_workbook(r"C:\Users\44774\Documents\Cambridge IIA\Advanced German\Zurich\Haltestellen - v2.xlsx")
sheet = wb.active
for row in range(2,759):
    ID = sheet['A' + str(row)].value
    name = sheet['C' + str(row)].value
    name = name.replace('Ã¼','ü')
    name = name.replace('Ã¶','ö')
    name = name.replace('Ã¤','ä')
    database[ID] = name

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