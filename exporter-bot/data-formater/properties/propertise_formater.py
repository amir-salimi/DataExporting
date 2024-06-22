#import modules
import pandas as pd
#reading the csv file
emp = pd.read_csv('./asli.csv')



data = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

emp.head()
emp.columns
result = emp.drop_duplicates(["part", "community", "area", "city"], keep="first").sort_values("part")
for i in result["part"]:
    print(i)
result.to_csv("/home/amir/Documents/export_data/exporter-bot/data-formater/pure.csv")   