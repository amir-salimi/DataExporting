import csv

import sqlite3

header = ['building_id', 'city', 'area', 'community', 'complex', 'building']

connection = sqlite3.connect("/home/amir/Desktop/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM buildings")

data = cursor.fetchall()

def get_community(id):
    cursor.execute(f"SELECT * FROM communities where id={id}")
    community = cursor.fetchall()
    return community

def get_area(id):
    cursor.execute(f"SELECT * FROM areas where id={id}")
    area = cursor.fetchall()
    return area

def get_city(id):
    cursor.execute(f"SELECT * FROM cities where id={id}")
    city = cursor.fetchall()
    return city


def get_complex(id):
    cursor.execute(f"SELECT * FROM complexs where id={id}")
    complex = cursor.fetchall()
    return complex


data_list = []

for i in data:
    building_id = i[0]
    if i[5] != None:
        community = get_community(i[5]) # i[5] -> community_id
    else:
        pass
    if i[3] != None:
        area = get_area(i[3]) # i[3] -> area_id
    else:
        pass
    city = get_city(i[4]) # i[4] -> city_id

    complex = ""
    print(community[0][1])
    print(area[0][1])
    print(city[0][1])

    data_list.append([building_id, city[0][1].lower(), area[0][1].lower(), community[0][1].lower(), complex.lower(), i[1].lower()])


file = "/home/amir/Documents/export_data/exporter-bot/data-formater/area_category/main.csv"


with open(file, 'w', newline="") as f:
    csvwriter = csv.writer(f) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data_list) # 5. write the rest of the data
