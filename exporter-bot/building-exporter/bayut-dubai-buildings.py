from bs4 import BeautifulSoup

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
import requests
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


def get_each_building_detail(link):
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
    

    requests.get(f"http://127.0.0.1:8000/building?link={link}&status={status}&name={name}&location={location}&about={about}")


def get_each_area_buildings(link):
    all_link = []
    try:
        for f in range(1, 21):
            time.sleep(1)
            search_link = None
            search_link = link + f"page/{f}/"
            driver.get(search_link)
            for f in driver.find_elements(By.CLASS_NAME, "absolute"):
                each_building_link = f.get_attribute("href")
                if each_building_link is not None:
                    all_link.append(each_building_link)
    except:
        pass
    for v in all_link:
        print(v)
        get_each_building_detail(v)


driver = chrome_webdriver()
driver.get("https://www.bayut.com/buildings/dubai/")

driver.find_element(By.CLASS_NAME, "scrollbar-hide").find_element(By.CLASS_NAME, "flex").click()
areas = driver.find_element(By.CLASS_NAME, "scrollbar-hide").find_element(By.CLASS_NAME, "grid").find_elements(By.TAG_NAME, "a")

area_link = []

for area in areas:
    area_link.append(area.get_attribute("href"))


for n in area_link:
    get_each_area_buildings(n)
