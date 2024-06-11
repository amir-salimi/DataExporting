import csv

import sqlite3

header = ['id', 'city', 'area', 'community', 'part', 'source']

connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_part")

data = cursor.fetchall()

def get_community(id):
    cursor.execute(f"SELECT * FROM area_community where id={id}")
    community = cursor.fetchall()
    return community

def get_area(id):
    cursor.execute(f"SELECT * FROM area_area where id={id}")
    area = cursor.fetchall()
    return area

def get_city(id):
    cursor.execute(f"SELECT * FROM area_city where id={id}")
    city = cursor.fetchall()
    return city

data_list = []

for i in data:
    id = i[0]
    part = i[1]
    community = get_community(i[2])[0][1]
    source = i[3]
    area = get_area(get_community(i[2])[0][2])[0][1]
    city = get_city(get_area(get_community(i[2])[0][2])[0][2])[0][1]
    # print("id : ", id, "| city : ", city, "| area : ", area, "| community : ", community, "| part : ", part, "| source : ", source)
    data_list.append([id, city, area, community, part, source])


file = "./Data.csv"


with open(file, 'w', newline="") as f:
    csvwriter = csv.writer(f) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data_list) # 5. write the rest of the data
