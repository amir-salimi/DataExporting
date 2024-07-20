import csv

import sqlite3

header = [
"id",
"name",
"source",
"city",
"area",
"community",
"link",
"status",
"location",
"about",
"images",
"highlights",
]

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



def get_detail(link):
    cursor.execute(f"SELECT * FROM building_details_info WHERE building_link LIKE '%{link}%'")
    about = cursor.fetchall()
    return about


def get_photo(link):
    cursor.execute(f"SELECT * FROM building_images WHERE building_link LIKE '%{link}%'")
    photo = cursor.fetchall()
    return photo


def get_highlight(link):
    cursor.execute(f"SELECT * FROM building_highlights WHERE building_link LIKE '%{link}%'")
    hightlights = cursor.fetchall()
    return hightlights


data_list = []

# print(get_photo('https://opr.ae/projects/emaar-anya-2-townhouses-in-arabian-ranches-3-dubai'))

for i in data:
    # break
    building_id = i[0]
    name = i[1] 
    source = i[2]
    area = get_area(i[3])[0][1]
    city = get_city(i[4])[0][1]
    print(city)
    if i[5] != None:
        community = get_community(i[5])[0][1]
    else:
        community = None

    link = i[6]
    about = i[7]
    location = i[9]
    status = i[10]
    

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

    data_list.append([building_id, name, source, city, area, community, link, status, location, about, image_list, highlights_list])
    

file = "/home/amir/Documents/export_data/exporter-bot/data-formater/buildings/main.csv"


with open(file, 'w', newline="") as f:
    csvwriter = csv.writer(f) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data_list) # 5. write the rest of the data

    