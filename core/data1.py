import sqlite3
import requests

connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM communities")

data = cursor.fetchall()


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
    community = i[1]
    cur = connection.cursor()
    cur.execute("SELECT * FROM area_part where is_ok=1")
    all_part = cur.fetchall()
    for part in all_part:
        if part[7] != None and part[5] == None:
            if community in part[7] and i[3]==part[3]:
                print(i)
                print(part)

        