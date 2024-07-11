from google import generativeai as genai


import sqlite3


connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM buildings")

data = cursor.fetchall()

all_part = []

api_key = "AIzaSyCbs1RJ1YzP8IySiCQFt09psTUXx0Xyzn4"


import google.generativeai as genai
import os

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

response = model.generate_content("give me a text")

# for i in data:
#     name = i[1]
#     desc = i[5]
#     print(name)
    # data = response.text.replace("```", "").replace("json", "")
    # r = model.generate_content(f"my building is {name} Building and my approximate address is {data}, so you give me more precise location: ?, gemini do not write any additional text")
    # print(r.text)
