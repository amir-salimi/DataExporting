#import modules
import pandas as pd
import csv
#reading the csv file
emp = pd.read_csv('./main.csv')

with open("./pure.csv", 'w') as csv_out:
    writer = csv.DictWriter(csv_out, fieldnames=["id", "building_id", "city", "area", "community", "complex", "building"])

emp.head()
emp.columns
result = emp.drop_duplicates(["building", "community", "area", "city"], keep="first")
result.to_csv("/home/amir/Documents/export_data/exporter-bot/data-formater/area_category/pure.csv")   