from google import generativeai as genai
import sqlite3


connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_building")

data = cursor.fetchall()

all_part = []




api_key = "AIzaSyB3LgXQ8-vO3ss5TJcHbtZLO3jOHwjjC1M"


import google.generativeai as genai
import os

genai.configure(api_key=api_key)



model = genai.GenerativeModel(model_name="gemini-1.5-flash")

for i in data:
    name = i[1]
    desc = i[5]
    print(name)

    response = model.generate_content(f"""is {name} Building is in which cities, areas, cimmunities of eua? its about that building -> {desc} gemini do not write any additional text and give me a json output""")

    # response = model.generate_content("give me location of Al Baraha Family Residence building on google maps")

    data = response.text.replace("```", "").replace("json", "")

    r = model.generate_content(f"my building is {name} Building and my approximate address is {data}, so you give me more precise location: ?, gemini do not write any additional text")

    print(r.text)

    # lat_long = model.generate_content(f"give me latitude and longitude of building with this data {r}, gemini do not write any additional text")


    # print(lat_long.text)