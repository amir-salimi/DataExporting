import csv

import sqlite3

header = ['id', 'building', 'link', 'area', 'description', 'bed', 'bath']

connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_unitofbuilding")

data = cursor.fetchall()

def get_photo(link):
    cursor.execute(f"SELECT * FROM area_unitphoto WHERE link LIKE '%{link}%'")
    photo = cursor.fetchall()
    return photo


def get_detail(link):
    cursor.execute(f"SELECT * FROM area_unitdetail WHERE link LIKE '%{link}%'")
    detail = cursor.fetchall()
    return detail


def get_building(id):
    cursor.execute(f"SELECT * FROM area_building WHERE id={id}")
    building = cursor.fetchall()
    return building

data_list = []

for i in data:
    id = i[0]   
    bed = i[1]
    bath = i[2]
    area = i[3]
    desc = i[4]
    link = i[5]
    building_id = i[6]
    building = get_building(building_id)[0][1]
    photo = get_photo(link)
    detail = get_detail(link)

    
    data_list.append([id, building.lower(), link.lower(), area.lower(), desc.lower(), bed.lower(), bath.lower()])


file = "/home/amir/Documents/export_data/exporter-bot/data-formater/units/main.csv"


with open(file, 'w', newline="") as f:
    csvwriter = csv.writer(f) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data_list) # 5. write the rest of the data
