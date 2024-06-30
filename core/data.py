import sqlite3
import requests

connection = sqlite3.connect("/home/amir/Documents/export_data/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_building")

data = cursor.fetchall()

# def get_building(id):
#     c = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
#     cur = c.cursor()
#     cur.execute(f"SELECT * FROM area_building WHERE id={id}")
#     building = cur.fetchall()
#     return building


def get_community(id):
    # c = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
    # cur = c.cursor()
    cursor.execute(f"SELECT * FROM area_community WHERE id={id}")
    community = cursor.fetchall()
    return community


def get_area(id):
    cursor.execute(f"SELECT * FROM area_area WHERE id={id}")
    area = cursor.fetchall()
    return area


def get_city(id):
    cursor.execute(f"SELECT * FROM area_city WHERE id={id}")
    city = cursor.fetchall()
    return city


for i in data:
    name = i[1]
    link = i[2]
    status = i[3]
    location = i[4]
    about = i[5]
    area = i[6]
    city = i[7]
    community = i[8]
    part = i[9]
    is_ok = i[10]
    if name != "None" and name != "HIGHLIGHTS":
        requests.get(f"http://127.0.0.1:8000/building?link={link}&status={status}&name={name}&location={location}&about={about}")
    
    # link = i[1]
    # h = i[2]
    # print(h)
    # requests.get(f"http://127.0.0.1:8000/building?link={link}&highlight={h}")

    # building_img = i[2]
    # building_link = i[1]
    # print(building_img)
    # requests.get(f"http://127.0.0.1:8000/building?link={building_link}&img={building_img}") # img and link

    # name = i[1]
    # source = i[2]
    # city = ...
    # area = ...
    # community_id = i[5]
    # community = get_community(community_id)
    # area = get_area(community[0][2])
    # city = get_city(area[0][2])
    # print(i)
    # requests.get(f"http://127.0.0.1:8000/city-prop/?city={city[0][1]}&area={area[0][1]}&community={community[0][1]}&part={name}&source={source}")


        