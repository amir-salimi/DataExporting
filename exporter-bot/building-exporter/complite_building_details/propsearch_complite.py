from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import sqlite3
import time
import os
import requests
import json

headers = {
    'Content-Type': 'application/json'
}   

connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")

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


def get_dubai_id():
    cr = connection.cursor()
    cr.execute(f"SELECT * FROM cities where name like 'dubai';")
    city = cr.fetchall()
    return city[0][0]


def get_complex_id_by_name(complex_name):
    cr = connection.cursor()
    cr.execute(f"SELECT * FROM complexs where name like '{complex_name}';")
    complex = cr.fetchall()
    return complex[0][0]


def get_building_detail_from_db_by_id(building_id):
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM buildings where id={building_id};")
    building = cur.fetchall()
    return building


def get_building_detail_from_db_by_name(building_name):
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM buildings where name like '{building_name}';")
    building = cur.fetchall()
    return building


def get_area(area_id):
    cr = connection.cursor()
    cr.execute(f"SELECT * FROM areas where id = {area_id};")
    area = cr.fetchall()
    return area[0][1]


def get_complex_buildings(complex_id):
    cr = connection.cursor()
    cr.execute(f"SELECT * FROM complexs_buildings where complex_id = {complex_id};") # get complex with complex_id
    complexs = cr.fetchall()
    building_id_list = []
    for c in complexs:
        building_id_list.append(c[2]) # n[2] -> building id
    return building_id_list


def go_to_search_input(search_input):
    driver.get("https://propsearch.ae/")
    input = driver.find_element(By.XPATH, "//*[@title='Search all of Dubai real estate']").click()
    time.sleep(1)
    input = driver.find_element(By.XPATH, "//*[@placeholder='Search anything']")
    input.send_keys(f"{search_input}")
    time.sleep(2)
    input.send_keys(Keys.ENTER)
    time.sleep(3)

driver = chrome_webdriver()


def get_detail(name, location, from_complex, c_n): # c_n -> complex_building2
    link = driver.current_url
    status = ""
    my_list = []
    try:
        all_main_detail = driver.find_element(By.ID, "location-guide-blueprint-main-image").text
        each_main_details = all_main_detail.split("\n")
        for each in range(len(each_main_details)):
            if each_main_details[each] == "Building type" :
                instance = each + 1
            if each_main_details[each] == "Status" :
                instance = each + 1
                status = each_main_details[instance]
            if each_main_details[each] == "Floors" :
                instance = each + 1
    except:
        status = None

    try:
        pose = driver.find_element(By.ID, "location-guide-blueprint-legacy-guide-section").find_element(By.CLASS_NAME, "ps-indent").text
        pose = pose.split("\n")[1:]
        about = ""
        for i in range(2, len(pose), 3):
            about += pose[i] + " "

        if from_complex == True:

            requests.post(
                url="http://127.0.0.1:8000/building/", 
                headers=headers, 
                data=json.dumps(
                    {
                        "city": "Dubai",
                        "area": str(location),
                        "name": str(name),
                        "building_link": str(link),
                        "status": str(status),
                        "location": str(location),
                        "about": str(about),
                        "source": "https://www.bayut.com/",
                        "publish_status": 1
                    }
                )  
            )            

            requests.patch(url=f"http://127.0.0.1:8000/complex/{get_complex_id_by_name(c_n)}/", headers=headers, data=json.dumps(
                {
                    "buildings" : [get_building_detail_from_db_by_name(name)[0][0]],
                }
            ))
            
        
        else:
            building_id = get_building_detail_from_db_by_name(name)[0][0]
            
            headers = {
                'Content-Type': 'application/json'
            }   

            put_data = json.dumps(
                {
                    "name": str(name),
                    "building_link": str(link),
                    "status": str(status),
                    "location": str(location),
                    "about": str(about),
                    "publish_status": 1,
                    "source": "https://propsearch.ae/"
                }
            )
            requests.put(url=f"http://127.0.0.1:8000/building/{building_id}/", headers=headers, data=put_data)
    except:
        pass


def get_building_detail_of_complex(complex_name):
    try:
        buildings_of_complex = driver.find_elements(By.CLASS_NAME, "shadow-ps-sm")
    except:
        buildings_of_complex = []

    all_building_of_complex_link = []
    for b in buildings_of_complex:
        all_building_of_complex_link.append(b.find_element(By.TAG_NAME, "a").get_attribute("href")) # add each of building_of_complex_link to a array

    for l in all_building_of_complex_link:
        driver.get(l)
        name_of_building = driver.find_element(By.ID, "location-guide-blueprint-title-section").find_element(By.TAG_NAME, "h1").text
        
        building_details = driver.find_element(By.ID, "location-guide-blueprint-legacy-guide-section").find_element(By.CLASS_NAME, "ps-indent").find_elements(By.CLASS_NAME, "flex")
        building_location = None
        for building_detail in building_details:
            if "Area" in building_detail.text:
                building_location = building_detail.text.replace("Area", "").replace("place", "").replace("\n", "")

        get_detail(name_of_building, building_location, from_complex=True, c_n=complex_name)


cursor = connection.cursor()
cursor.execute("SELECT * FROM buildings;")
data = cursor.fetchall()


for i in data: 
    if i[7] == 0:
        if i[10] == get_dubai_id():
            go_to_search_input(i[1])
            if driver.current_url != "https://propsearch.ae/":
                get_detail(name=i[1], location=i[5], from_complex=None, c_n=None)


cursor = connection.cursor()
cursor.execute("SELECT * FROM complexs;")
data = cursor.fetchall()


for complex in data:
    complex_id = complex[0]
    complex_name = complex[1]

    building_list_id = get_complex_buildings(complex_id)
    complex_is_ok = None

    for building_id in building_list_id:
        if get_building_detail_from_db_by_id(building_id)[0][3] == None:
            complex_is_ok = False
            break
    
    if complex_is_ok == False and complex[2] == 0:
        go_to_search_input(complex_name)
        get_building_detail_of_complex(complex_name)
        complex_id = get_complex_id_by_name(complex_name)
        requests.patch(f"http://127.0.0.1:8000/complex/{complex_id}/", headers=headers, data=json.dumps({"publish_status" : 1}))





