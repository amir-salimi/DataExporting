#import modules
import pandas as pd
#reading the csv file
emp = pd.read_csv('./asli.csv')

emp.head()
emp.columns
result = emp.drop_duplicates(["part", "community", "area", "city"], keep="first")
result.to_csv("/home/amir/Documents/export_data/exporter-bot/data-formater/properties/pure.csv")   