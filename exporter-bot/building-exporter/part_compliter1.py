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
cursor.execute("SELECT * FROM area_part")

data = cursor.fetchall()


driver = chrome_webdriver()


def get_each_building_detail(link, building_name_db):
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
    

    requests.get(f"http://127.0.0.1:8000/building?link={link}&status={status}&name={building_name_db}&location={location}&about={about}")




def get_building_link(building_name_db):
    try:
        all_guide_link = driver.find_element(By.XPATH, "//*[@aria-label='Guide links']")
        building_name = driver.find_element(By.XPATH, "//*[@aria-label='Filter label']")
        building_link = all_guide_link.find_element(By.XPATH, f"//*[@title='{building_name.text}']").get_attribute("href")
        get_each_building_detail(building_link, building_name_db)
    except:
        pass

    
for i in data: 
    if i[6] == None and i[0]<1001:
        print(i[0])
        driver.get("https://www.bayut.com/")
        time.sleep(5)
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
                get_building_link(i[1])
        else:
            get_building_link(i[1])