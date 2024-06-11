#import modules
import pandas as pd
#reading the csv file
emp = pd.read_csv('./Data.csv')

data = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

emp.head()
emp.columns
result = emp.drop_duplicates(["part"], keep="first")
for i in result["part"]:
    print(i)
result.to_csv("./new.csv")