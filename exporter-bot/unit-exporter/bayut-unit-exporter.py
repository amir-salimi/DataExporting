from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys

import os
import ast
import time
import requests
import sqlite3
import pandas as pd

def chrome_webdriver():
    chromedriver_path = os.getcwd()+"/chromedriver"
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    options.add_argument(f'user-agent={user_agent}')
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def is_ok(building):
    if building != None:
        is_ok_building = building

    if is_ok_building:
        try:
            requests.get(f"http://127.0.0.1:8000/building-unit?is_ok={True}&building_name={is_ok_building}")
        except:
            pass



driver = chrome_webdriver()
connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM buildings")
data = cursor.fetchall()


def get_agency_bio(agency_bio_link):

    driver.get(agency_bio_link)
    
    agency_name = driver.find_element(By.XPATH, "//*[@aria-label='Agency name']").text
    agency_img = driver.find_element(By.XPATH, f"//*[@aria-label='Agency logo']").get_attribute("src")

    driver.find_element(By.XPATH, "//span[text()='Read all']").click()
    
    try:
        driver.find_element(By.XPATH, "//span[text()='See all areas']").click()
    except:
        pass

    time.sleep(5)


    agency_details = driver.find_elements(By.XPATH, "//div[@dir='ltr']")


    agency_details_list = []

    for detail in agency_details:
        agency_detail = detail.text
        if "Read less" in agency_detail:
            agency_detail = agency_detail.replace("Read less", "")
        if "See less areas" in agency_detail:
            agency_detail = agency_detail.replace("See less areas", "")
        if "BRN" in agency_detail:
            agency_detail = agency_detail.replace("\n", "")
        agency_detail = agency_detail.replace("&", "and").replace("'", "")
        agency_details_list.append(agency_detail)

    if "Description" in str(agency_details_list):
        print("ok")
    else:
        print("repeat...")
        get_agency_bio(agency_bio_link)


    driver.find_element(By.XPATH, "//button[@aria-label='Call']").click()

    time.sleep(3)
    agency_phone_number = driver.find_element(By.XPATH, "//*[@aria-label='Listing phone number']").text

    # print("agency : ")
    print("agency_bio_link : ", agency_bio_link)
    # print("agency_name : ", agency_name)
    # print("agency_img : ", agency_img)
    # print("agency_phone_number : ", agency_phone_number)
    print("agency_details_list : ", agency_details_list)
    

    print("//////////////////////////")

    requests.get(f"http://127.0.0.1:8000/agency/?name={agency_name}&link={agency_bio_link}&phone_number={agency_phone_number}&details={agency_details_list}&agency_photo={agency_img}")


def get_agent_bio(agent_bio_link):
    driver.get(agent_bio_link)

    agency_name = driver.find_element(By.XPATH, "//*[@aria-label='Agency name']").text
    agency_bio_link = driver.find_element(By.XPATH, "//*[@aria-label='Agency name']").find_element(By.TAG_NAME, "a").get_attribute("href")
    get_agency_bio(agency_bio_link)

    driver.get(agent_bio_link)

    agent_name = driver.find_element(By.XPATH, "//*[@aria-label='Agent name']").text
    try:
        agent_img = driver.find_element(By.XPATH, f"//*[@aria-label='Agent {agent_name}']").get_attribute("src")
    except:
        agent_img = None

    driver.find_element(By.XPATH, "//span[text()='Read all']").click()    
    try:
        driver.find_element(By.XPATH, "//span[text()='See all areas']").click()
    except:
        pass
    time.sleep(5)

    agent_details = driver.find_elements(By.XPATH, "//div[@dir='ltr']")

    driver.find_element(By.XPATH, "//*[@aria-label='Call']").click()
    time.sleep(3)
    agent_phone_number = driver.find_element(By.XPATH, "//*[@aria-label='Listing phone number']").text
    agent_details_list = []

    for detail in agent_details:
        agent_detail = detail.text
        if "Read less" in agent_detail:
            agent_detail = agent_detail.replace('Read less', '')
        if "BRN" in agent_detail:
            agent_detail = agent_detail.replace('\n', '')
        agent_detail = agent_detail.replace("&", "and")
        agent_details_list.append(agent_detail)

    newList = [item.replace("'", '"') for item in agent_details_list]
    

    print("agent : ")
    print("agency_name : ", agency_name)
    print("agency_bio_link : ", agency_bio_link)
    print("agent_name : ", agent_name)
    print("agent_img : ", agent_img)
    print("agent_phone_number : ", agent_phone_number)
    print("agent_details_list : ", newList)   
    

    print("////////////////////////////")

    requests.get(f"http://127.0.0.1:8000/agent/?name={agent_name}&link={agent_bio_link}&phone_number={agent_phone_number}&details={newList}&agent_photo={agent_img}&agency_link={agency_bio_link}")
    

def get_each_prop_detail(all_link, building_name):
    for link in all_link:
            complex = None
            agency_bio_link = None
            driver.get(link)
            price = driver.find_element(By.XPATH, "//*[@aria-label='Price']").text
            location = driver.find_element(By.XPATH, "//*[@aria-label='Property header']").text
            bed = driver.find_element(By.XPATH, "//*[@aria-label='Beds']").text
            bath = driver.find_element(By.XPATH, "//*[@aria-label='Baths']").text
            unit_area = driver.find_element(By.XPATH, "//*[@aria-label='Area']").text
            price = driver.find_element(By.XPATH, "//*[@aria-label='Price']").text
            desc = driver.find_element(By.XPATH, "//*[@aria-label='Property description']").text
            location = location.split(",")

            agent_bio_link = driver.find_element(By.XPATH, "//*[@aria-label='Agent name']").get_attribute("href")
            if agent_bio_link is None:
                agency_bio_link = driver.find_element(By.XPATH, "//*[@aria-label='View all properties']").get_attribute("href")
                
    

            if len(location) == 5:
                name = location[0]
                complex = location[1]
                community = location[2]
                area = location[3]
                city = location[4]

            elif len(location) == 4:
                name = location[0]
                community = location[1]
                area = location[2]
                city = location[3]

            elif len(location) == 3:
                name = location[0]
                area = location[1]
                city = location[2]
                community = None
            
            else:
                name = None
                area = None
                city = None
                community = None
                complex = None

            if name != None:
                if name[0] == " ":
                    name = name[1:]
            if complex != None:
                
                if complex[0] == " ":
                    complex = complex[1:]

            if community != None:
                if community[0] == " ":
                    community = community[1:]

            if area != None:
                if area[0] == " ":
                    area = area[1:]

            if city != None:
                if city[0] == " ":
                    city = city[1:]
       

            prop_detials = driver.find_element(By.XPATH, "//*[@aria-label='Property details']").find_elements(By.TAG_NAME, "li")

            for prop_detail in prop_detials:
                prop_detail = prop_detail.text.split("\n")
                key = prop_detail[0]
                value = prop_detail[1]
                requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&key={key}&value={value}")

            time.sleep(3)
            driver.find_element(By.XPATH, "//*[@aria-label='View gallery']").click() # opening photos window
            photos = driver.find_element(By.XPATH, "//*[@aria-label='Gallery dialog photo grid']").find_elements(By.TAG_NAME, "img")

            for photo in photos:
                photo = photo.get_attribute("src")
                requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&img={photo}")
        

            
            try:
                get_agent_bio(agent_bio_link)
            except:
                get_agency_bio(agency_bio_link)

            print(agent_bio_link)
            print(agency_bio_link)

            if building_name and area and city is not None:
                req = requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&agency_link={agency_bio_link}&agent_link={agent_bio_link}&building_name={building_name}&building_link={None}&community={community}&area={area}&city={city}&bed={bed}&bath={bath}&price={price}&description={desc}&unit_area={unit_area}&complex_name={complex}&price={price}")
                if req.status_code == 500:
                    req = requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&agency_link={agency_bio_link}&agent_link={agent_bio_link}&building_name={building_name}&building_link={None}&community={community}&area={area}&city={city}&bed={bed}&bath={bath}&price={price}&description={desc}&unit_area={unit_area}&complex_name={complex}&price={price}")
    
    
    is_ok(building_name)

           
def get_each_prop(building_name):
    all_link = []
    time.sleep(5)
    
    a = driver.find_elements(By.XPATH, "//*[@aria-label='Listing']")
    for n in a:
        link = n.find_element(By.TAG_NAME, "a").get_attribute("href")
        all_link.append(link)

    while True:
        try:
            driver.find_element(By.XPATH, "//*[@title='Next']").click()
            a = driver.find_elements(By.XPATH, "//*[@aria-label='Listing']")
            time.sleep(8)
            for n in a:
                link = n.find_element(By.TAG_NAME, "a").get_attribute("href")
                all_link.append(link)
        except:
            break
    get_each_prop_detail(all_link, building_name)


def go_to_search_input(search_input):
    driver.get("https://www.bayut.com/")
    input = driver.find_element(By.XPATH, "//*[@placeholder='Enter location']")
    input.send_keys(f"{search_input}")
    time.sleep(4)
    input.send_keys(Keys.SPACE)
    time.sleep(10)
    input.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@aria-label='Find button']").click()
    time.sleep(1)


for i in data: 
    
    if i[7] == 1:
        print(i[0])
        go_to_search_input(i[1])
        get_each_prop(i[1])



