from bs4 import BeautifulSoup

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
import requests
import os

from sentry_tool.sentry_confiuration import configuration

configuration("https://48b901e268fd490dd37803bd38674eea@o4507526316883968.ingest.us.sentry.io/4507582717820928")


CITY_NAME = "Dubai"



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
    time.sleep(1)
    link = driver.current_url
    if "area-guides" in link:
        pass
    else:
        try: # if the bot does not find highlights value return None 
            highlights = driver.find_element(By.CLASS_NAME, "markdown-elements").text
            highlights = highlights.split("\n")
            for highlight in highlights: # link and highlight
                requests.get(f"http://127.0.0.1:8000/building?link={link}&highlight={highlight}")
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
        if "," in m[1]:
            try:
                name = m[1].split(",")[0].replace("&", "")
                if name[0] == " ":
                    name = name[1:]
            except:
                name = None
            try:
                location = m[1].split(",")[1]
                if location[0] == " ":
                    location = location[1:]
            except:
                location = None

        else:
            name = m[1]
            location = CITY_NAME
            area = CITY_NAME


        try: # if the bot does not find img value, pass
            img = driver.find_elements(By.TAG_NAME, "img")
            for i in img:
                image = i.get_attribute("src")
                if "jpg" in image and image != "https://assets.bayut.com/content/Dubai_Transactions_my_Bayut_desktop_EN_2ec3b1edfd_4a056a94b2_50773e1f3d.jpg?w=3840":
                    requests.get(f"http://127.0.0.1:8000/building?link={link}&img={image}") # img and link
        except:
            pass

        try:
            about = driver.find_elements(By.CLASS_NAME, "markdown-elements")[1].text.replace("&", "")
        except:
            about = None
    
        try:
            nutshells = driver.find_elements(By.CLASS_NAME, "markdown-elements")[3].text
            for nutshell in nutshells.split("\n"):
                nutshell = nutshell.split(":") # nutshell -> key, value
                key = nutshell[0]
                value = nutshell[1]
                requests.get(f"http://127.0.0.1:8000/building?link={link}&key={key}&value={value}")
        except:
            pass
        

        requests.get(f"http://127.0.0.1:8000/building?link={link}&status={status}&name={name}&location={location}&about={about}&city={CITY_NAME}&source=https://www.bayut.com/")


def get_each_area_buildings(link, main_page):
    all_link = []
    for f in range(1, 21):
        time.sleep(1)
        search_link = None
        search_link = link + f"page/{f}/"
        driver.get(search_link)

        try:
            time.sleep(3)
            page_text = driver.find_element(By.CLASS_NAME, "mx-auto").text
            if page_text == "Sorry, we couldn't find the page you're trying to view. You can just specify the new search criteria." :
                    break
        except:
            pass

        for f in driver.find_elements(By.CLASS_NAME, "absolute"):
            each_building_link = f.get_attribute("href")
            if each_building_link is not None:
                all_link.append(each_building_link)

    for each_link in all_link:
        get_each_building_detail(each_link)


driver = chrome_webdriver()
driver.get(f"https://www.bayut.com/buildings/{CITY_NAME.lower()}/")

main_page = driver.page_source


driver.find_element(By.CLASS_NAME, "scrollbar-hide").find_element(By.CLASS_NAME, "flex").click() # to show all location 
areas = driver.find_element(By.CLASS_NAME, "scrollbar-hide").find_element(By.CLASS_NAME, "grid").find_elements(By.TAG_NAME, "a") # get all areas

area_link = []

for area in areas:
    area_link.append(area.get_attribute("href")) # get link of each area and append it to area_link list


for n in area_link:
    get_each_area_buildings(n, main_page) 
