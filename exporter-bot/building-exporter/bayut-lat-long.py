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
cursor.execute("SELECT * FROM area_building")

data = cursor.fetchall()



driver = chrome_webdriver()
url = "https://www.bayut.com/for-sale/residential-building/uae/?map_active=true"


driver.get(url)


for i in data:
    input = driver.find_element(By.XPATH, "//*[@placeholder='Enter location']")
    input.send_keys(f"{i[1]} ")
    time.sleep(5)
    input.send_keys(Keys.ENTER)
    
    try:
        current = urlparse(driver.current_url)
        lat = parse_qsl(current.query)["center_lat"]
        long = parse_qsl(current.query)["center_long"]
        
    except:
        time.sleep(7)
        current = str(urlparse(driver.current_url))
        print(current)
        lat = parse_qsl(current.query)["center_lat"]
        long = parse_qsl(current.query)["center_long"]

    print(lat)
    print(long)
    break


time.sleep(50)