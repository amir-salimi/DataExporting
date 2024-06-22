import csv

import sqlite3

header = [
"id",
"name",
"link",
"status",
"location",
"about",
"details",
"images",
"highlights",
]

connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_building")

data = cursor.fetchall()



def get_detail(link):
    cursor.execute(f"SELECT * FROM area_detail WHERE link LIKE '%{link}%'")
    about = cursor.fetchall()
    return about


def get_photo(link):
    cursor.execute(f"SELECT * FROM area_buildingimg WHERE link LIKE '%{link}%'")
    photo = cursor.fetchall()
    return photo


def get_highlight(link):
    cursor.execute(f"SELECT * FROM area_highlight WHERE link LIKE '%{link}%'")
    photo = cursor.fetchall()
    return photo


data_list = []

# print(get_photo('https://opr.ae/projects/emaar-anya-2-townhouses-in-arabian-ranches-3-dubai'))

for i in data:
    id = i[0]
    name = i[1] 
    link = i[2]
    status = i[3]
    location = i[4]
    about = i[5]

    details = get_detail(link)
    detail_list = []
    for d in details:
        detail = d[1] + " : " + d[2]
        detail_list.append(detail)
    
    image_links = get_photo(link)
    image_list = []
    for i in image_links:
        image_list.append(i[2])

    highlights = get_highlight(link)
    highlights_list = []
    for h in highlights:
        highlights_list.append(h[2])

    if name != None :
        if status == "Ready" or status == "off-paln":
            data_list.append([id,name,link, status, location, about, detail_list, image_list, highlights_list])
    

file = "/home/amir/Documents/export_data/exporter-bot/data-formater/buildings/main-buildings.csv"


with open(file, 'w', newline="") as f:
    csvwriter = csv.writer(f) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data_list) # 5. write the rest of the data
