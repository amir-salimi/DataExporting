import sqlite3
import requests

connection = sqlite3.connect("/home/amir/Documents/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_unitphoto")

data = cursor.fetchall()

# def get_building(id):
#     c = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
#     cur = c.cursor()
#     cur.execute(f"SELECT * FROM area_building WHERE id={id}")
#     building = cur.fetchall()
#     return building


for i in data:
    link = i[1]
    img = i[2]
    requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&img={img}")
    # requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&key={key}&value={value}")


# for i in data:
#     # print(i)
    
#     buildign_id = i[6]    

#     print(get_building(buildign_id))