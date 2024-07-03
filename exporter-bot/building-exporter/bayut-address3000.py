from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from urllib.parse import urlparse, parse_qsl


import requests
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
cursor.execute("SELECT * FROM buildings")

data = cursor.fetchall()



driver = chrome_webdriver()


all_building_name = []

def get_address(building):
    try:
        a = driver.find_element(By.XPATH, "//*[@aria-label='Listing']").find_element(By.XPATH, "//*[@aria-label='Location']")
        cursor.execute(f"SELECT * FROM buildings WHERE id={building[0]}")
        building = cursor.fetchall()

        if str(building[0][4]).lower() in a.text.lower():
            all_address = a.text.split(",")
            building_name = building[0][1]

            if len(all_address) == 3:
                area = all_address[1][1:]
                city = all_address[2][1:]
                community = None

            if len(all_address) == 4:
                community = all_address[1][1:]
                area = all_address[2][1:]
                city = all_address[3][1:]
            
            print(building_name)
            print(community)
            print(area)
            print(city)
            requests.get(f"http://127.0.0.1:8000/city-prop/?building_name={building_name}&community={community}&area={area}&city={city}")
    except:
        pass
             

for i in data: 
    try:
        if i[4] != "None" and 2787 < i[0] < 3000 and i[6] == 0:
            print(i[0])
            driver.get("https://www.bayut.com/")
            input = driver.find_element(By.XPATH, "//*[@placeholder='Enter location']")
            input.send_keys(f"{i[1]}")
            time.sleep(2)
            input.send_keys(Keys.SPACE)
            time.sleep(5)
            input.send_keys(Keys.ENTER)
            time.sleep(3)
            driver.find_element(By.XPATH, "//*[@aria-label='Find button']").click()
            time.sleep(5)


            if driver.current_url == "https://www.bayut.com/for-sale/property/uae/":
                driver.get("https://www.bayut.com/")
                input = driver.find_element(By.XPATH, "//*[@placeholder='Enter location']")
                input.send_keys(f"{i[1]}")
                time.sleep(5)
                input.send_keys(Keys.ENTER)
                time.sleep(3)
                driver.find_element(By.XPATH, "//*[@aria-label='Find button']").click()
                time.sleep(5)
                a = driver.find_element(By.XPATH, "//*[@aria-label='Listing']").find_element(By.XPATH, "//*[@aria-label='Location']")
                if driver.current_url == "https://www.bayut.com/for-sale/property/uae/":
                    pass
                else:
                    get_address(i)
            else:
                get_address(i)

    except:
        pass    
        