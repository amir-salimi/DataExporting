from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from urllib.parse import urlparse, parse_qsl

import sqlite3
import time
import os


def chrome_webdriver():
    chromedriver_path = os.getcwd()+"/chromedriver"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/123.0.0.0 Safari/537.36'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    options.add_argument(f'user-agent={user_agent}')
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_part")

data = cursor.fetchall()
driver = chrome_webdriver()

import requests

def get_detail(name, location):
    link = driver.current_url
    status = ""
    my_list = []
    try:
        all_main_detail = driver.find_element(By.ID, "location-guide-blueprint-main-image").text
        each_main_details = all_main_detail.split("\n")
        for each in range(len(each_main_details)):
            if each_main_details[each] == "Building type" :
                instance = each + 1
                print("type = ", each_main_details[instance])

            if each_main_details[each] == "Status" :
                instance = each + 1
                status = each_main_details[instance]

            if each_main_details[each] == "Floors" :
                instance = each + 1
                print("floors = ", each_main_details[instance])
    except:
        status = None
    try:
        pose = driver.find_element(By.ID, "location-guide-blueprint-legacy-guide-section").find_element(By.CLASS_NAME, "ps-indent").text
        pose = pose.split("\n")[1:]
        about = ""
        for i in range(2, len(pose), 3):
            about += pose[i] + " "
        requests.get(f"http://127.0.0.1:8000/building?link={link}&status={status}&name={name}&location={location}&about={about}")
    except:
        pass

# for i in data: 
#     if i[8] == 0 and i[0] >= 1453:
#         if i[4] == 3 or i[4] == 4 or i[4] == 5 :
#             print(i[0])
#             driver.get("https://propsearch.ae/")
#             input = driver.find_element(By.XPATH, "//*[@title='Search all of Dubai real estate']").click()
#             time.sleep(1)
#             input = driver.find_element(By.XPATH, "//*[@placeholder='Search anything']")
#             input.send_keys(f"{i[1]}")
#             time.sleep(2)
#             input.send_keys(Keys.ENTER)
#             time.sleep(3)
#             if driver.current_url != "https://propsearch.ae/":
#                 get_detail(i[1], i[9])


# for i in data:
#     try:
#         if i[6]!= "" and i[7] == "" and i[0]>1442 and i[8] == 1:
#             print(i[0])
#             print(i[6])
#             driver.get(i[6])
#             if driver.current_url != "https://propsearch.ae/":
#                 get_detail(i[1], i[9])
#     except:
#         pass


for i in data:
    try:
        if i[7] == None and i[8] == 1 and "https://propsearch.ae/" in i[6]:
            print(i[0])
            print(i[6])
            driver.get(i[6])
            if driver.current_url != "https://propsearch.ae/":
                get_detail(i[1], i[9])
    except:
        pass