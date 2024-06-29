from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


from subprocess import call

import time
import requests
import os
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

driver = chrome_webdriver()


connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM area_building")

data = cursor.fetchall()


def get_each_building_detail(link, building_name):
    driver.get(link)
    try:
        highlights = driver.find_element(By.CLASS_NAME, "markdown-elements").text
        highlights = highlights.split("\n")
        for h in highlights: # link and highlight
            requests.get(f"http://127.0.0.1:8000/building?link={link}&highlight={h}")
        # [print(h) for h in highlights] # link and highlight
    except:
        highlights = None

    try:
        m = driver.find_elements(By.CLASS_NAME, "container")[2].text
        m = m.split("\n")
    except:
        pass

    try:
        status = m[0]
    except:
        status = None
    try:
        name = m[1].split(",")[0]
    except:
        name = None
    try:
        location = m[1].split(",")[1]
    except:
        location = None

    try:
        img = driver.find_elements(By.TAG_NAME, "img")
        for i in img:
            image = i.get_attribute("src")
            if "jpg" in image and image != "https://assets.bayut.com/content/Dubai_Transactions_my_Bayut_desktop_EN_2ec3b1edfd_4a056a94b2_50773e1f3d.jpg?w=3840":
                requests.get(f"http://127.0.0.1:8000/building?link={link}&img={image}") # img and link
                pass
    except:
        pass

    try:
        about = driver.find_elements(By.CLASS_NAME, "markdown-elements")[1].text
    except:
        about = None

    try:
        nutshells = driver.find_elements(By.CLASS_NAME, "markdown-elements")[3].text
        for nutshell in nutshells.split("\n"):
            nutshell = nutshell.split(":") # nutshell key and value
            key = nutshell[0]
            value = nutshell[1]
            requests.get(f"http://127.0.0.1:8000/building?link={link}&key={key}&value={value}")
    except:
        pass
    
    if name == None or name == "HIGHLIGHTS":
        name = building_name
    
    requests.get(f"http://127.0.0.1:8000/building?link={link}&status={status}&name={name}&location={location}&about={about}")

    return driver.current_url


def is_ok(building):
    if building != None:
        is_ok_building = building

    if is_ok_building:
        try:
            requests.get(f"http://127.0.0.1:8000/building-unit?is_ok={True}&building_name={is_ok_building}")
        except:
            pass




def get_each_prop_detail(all_link, building_name):
    
    for link in all_link:
        try:
            driver.get(link)
            price = driver.find_element(By.XPATH, "//*[@aria-label='Price']").text
            location = driver.find_element(By.XPATH, "//*[@aria-label='Property header']").text
            bed = driver.find_element(By.XPATH, "//*[@aria-label='Beds']").text
            bath = driver.find_element(By.XPATH, "//*[@aria-label='Baths']").text
            unit_area = driver.find_element(By.XPATH, "//*[@aria-label='Area']").text
            desc = driver.find_element(By.XPATH, "//*[@aria-label='Property description']").text
            location = location.split(",")

            if len(location) == 4:
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
            
            prop_detials = driver.find_element(By.XPATH, "//*[@aria-label='Property details']").find_elements(By.TAG_NAME, "li")

            for prop_detail in prop_detials:
                prop_detail = prop_detail.text.split("\n")
                key = prop_detail[0]
                value = prop_detail[1]
                requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&key={key}&value={value}")


            try:
                building_link_in_page = driver.find_element(By.XPATH, f"//*[@title='{name}']").get_attribute("href")

                
                curs = connection.cursor()
                curs.execute(f"SELECT * FROM area_building WHERE link LIKE '%{building_link_in_page}%'")
                building = curs.fetchall() 
                
                if building != []:
                    main_building_name = building_name
                    building_current_link = building[0][2]
                else:
                    building_current_link = get_each_building_detail(building_link_in_page, building_name)
                    main_building_name = building_name
                    
            except:
                main_building_name = name
                building_current_link = None


            time.sleep(3)
            driver.find_element(By.XPATH, "//*[@aria-label='View gallery']").click() # opening photos window
            photos = driver.find_element(By.XPATH, "//*[@aria-label='Gallery dialog photo grid']").find_elements(By.TAG_NAME, "img")

            for photo in photos:
                photo = photo.get_attribute("src")
                requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&img={photo}")

            time.sleep(5)
            if main_building_name and area and city is not None:
                req = requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&building_name={main_building_name}&building_link={building_current_link}&community={community}&area={area}&city={city}&bed={bed}&bath={bath}&price={price}&description={desc}&unit_area={unit_area}")
                if req.status_code == 500:
                    main_building_name = building_name
                    req = requests.get(f"http://127.0.0.1:8000/building-unit?link={link}&building_name={main_building_name}&building_link={building_current_link}&community={community}&area={area}&city={city}&bed={bed}&bath={bath}&price={price}&description={desc}&unit_area={unit_area}")
        except:
            pass
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


for i in data: 
    if i[0] < 1400 and i[0] > 699 and i[10] == 0:
        print(i[0])
        driver.get("https://www.bayut.com/")
        input = driver.find_element(By.XPATH, "//*[@placeholder='Enter location']")
        input.send_keys(f"{i[1]}")
        time.sleep(10)
        input.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@aria-label='Find button']").click()
        get_each_prop(i[1])

        # driver.get("https://www.bayut.com/")
        # input = driver.find_element(By.XPATH, "//*[@placeholder='Enter location']")
        # input.send_keys(f"{i[1]}")
        # time.sleep(5)
        # input.send_keys(Keys.ENTER)
        # driver.find_element(By.XPATH, "//*[@aria-label='To rent']").click()
        # driver.find_element(By.XPATH, "//*[@aria-label='Find button']").click()
        # time.sleep(5)                                                                                                                                                 