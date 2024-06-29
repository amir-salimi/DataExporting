import sqlite3
import requests

connection = sqlite3.connect("/home/amir/Documents/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_unitofbuilding")

data = cursor.fetchall()

def get_building(id):
    c = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
    cur = c.cursor()
    cur.execute(f"SELECT * FROM area_building WHERE id={id}")
    building = cur.fetchall()
    return building





for i in data:
    # print(i)
    bed = i[1]
    bath = i[2]
    area = i[3]
    desc = i[4]
    link = i[5]
    building = get_building(i[6])

    if building != []:
        print(building[0][8])
        building = building[0][1]

        # requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&building_name={building}&building_link={link}&community={community}&area={area}&city={city}&bed={bed}&bath={bath}&price={price}&description={desc}&unit_area={unit_area}")