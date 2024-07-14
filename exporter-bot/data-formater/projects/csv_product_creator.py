import csv

import sqlite3

header = [
"id",
"name",
"location",
"developer",
"link",
"price",
"per_meter_price",
"area",
"payment_plan",
"bed_room",
"category",
"handover",
"views",
"city",
"status",
"approximate_location",
"developer_project_number",
"development",
"updated_at",
"finish",
"type",
"created_at",
"frequently_qustion",
"photo",
"plan_map",
"about",]

connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM export_product")

data = cursor.fetchall()

def get_category(id):
    cursor.execute(f"SELECT * FROM export_category where id={id}")
    category = cursor.fetchall()

    return category

def get_status(id):
    cursor.execute(f"SELECT * FROM export_status where id={id}")
    area = cursor.fetchall()
    return area



def get_frequently_qustion(link):
    print(link)
    cursor.execute(f"SELECT * FROM export_answerandquestion WHERE link LIKE '%{link}%'")
    question = cursor.fetchall()
    return question

def get_about(link):
    print(link)
    cursor.execute(f"SELECT * FROM export_about WHERE link LIKE '%{link}%'")
    about = cursor.fetchall()
    return about


def get_photo(link):
    print(link)
    cursor.execute(f"SELECT * FROM export_productphoto WHERE link LIKE '%{link}%'")
    photo = cursor.fetchall()
    return photo


def get_plan_map(link):
    print(link)
    cursor.execute(f"SELECT * FROM export_productplanmap WHERE link LIKE '%{link}%'")
    plan = cursor.fetchall()
    return plan




data_list = []

# print(get_photo('https://opr.ae/projects/emaar-anya-2-townhouses-in-arabian-ranches-3-dubai'))

for i in data:
    # break
    id = i[0]
    name = i[1] 
    location = i[2]
    developer = i[3]
    link = i[4]
    price = i[5]
    per_meter_price = i[6]
    area = i[7]
    payment_plan = i[8]
    bed_room = i[9]
    handover = i[10]
    views = i[11]
    city = i[12]
    approximate_location = i[13]
    development = i[14]
    developer_project_number = i[15]
    updated_at = i[16]
    type = i[17]
    finish = i[18]
    if i[19] is not None:
        category = get_category(i[19])
    else:
        category = None
        
    if i[20] is not None:
        status = get_status(i[20]) 
    else:
        status = None
    created_at = i[21]

    try:
        frequently_qustion = get_frequently_qustion(link)
    except:
        frequently_qustion = None
    try:
        photo = get_photo(link)
    except:
        photo = None
    try:
        plan_map = get_plan_map(link)
    except:
        plan_map = None
    try:
        about = get_about(link)
    except:
        about = None 
    data_list.append([id,name,location,developer,link,price,per_meter_price,area,payment_plan,bed_room,category,handover,views,city,status,approximate_location,developer_project_number,development,updated_at,finish,type,created_at,frequently_qustion,photo,plan_map,about])
    


file = "/home/amir/Documents/export_data/exporter-bot/data-formater/products/main-products.csv"


with open(file, 'w', newline="") as f:
    csvwriter = csv.writer(f) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data_list) # 5. write the rest of the data
