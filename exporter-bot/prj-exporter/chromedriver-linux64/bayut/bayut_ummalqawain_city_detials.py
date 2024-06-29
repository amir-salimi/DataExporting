from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import TimeoutException

from subprocess import call

import time
import requests
import os

import pandas as pd


def chrome_webdriver():
    chromedriver_path = os.getcwd()+"/chromedriver"
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    options.add_argument(f'user-agent={user_agent}')
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


url = 'https://www.bayut.com/for-sale/property/uae/'

driver = chrome_webdriver()

def get_properties(url, drop_down):
    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
    except TimeoutException:
        get_properties(url=url, drop_down=drop_down)
    try:
        driver.find_elements(By.CLASS_NAME, "_44977ec6")[1].click() # click for view more
    except:
        pass
    try:
        props = driver.find_element(By.XPATH, "//*[@aria-label='Location links']").find_elements(By.TAG_NAME, "a")
        return props
    except:
        return None


def get_prop_list(url, drop_down):
    pros = get_properties(url=url, drop_down=drop_down)
    try:
        prop_list = [[c.text.split("\n")[0], c.get_attribute("href")] for c in pros if c.text.split("\n")[0] != ''] # cleaning propertice and get cities and links
        return prop_list
    except:
        return None
    

prop_list = get_prop_list(url=url, drop_down=False) # get cities and save text and link of them to a list

if prop_list is not None:
    for p in prop_list:
        city = p[0]
        city_link = p[1]
        if city == "Umm Al Qawain":
            area_list = get_prop_list(url=city_link, drop_down=False) # get areas and save text and link of them to a list
            if area_list is not None:
                for area in area_list:
                    area_link = area[1]
                    community_list = get_prop_list(area_link, drop_down=False) # get community and save text and link of them to a list
                    if community_list is not None: # we have 3 category and subcategory
                        for community in community_list:
                            part_list = get_prop_list(url=community[1], drop_down=False) # get part and save text and link of them to a list
                            if part_list is not None: # we have 4 category and subcategory
                                for part in part_list:
                                    requests.get(f"http://127.0.0.1:8000/city-prop/?city={city}&area={area[0]}&community={community[0]}&part={part[0]}&source=https://www.bayut.com/")
                            else:
                                requests.get(f"http://127.0.0.1:8000/city-prop/?city={city}&area={area[0]}&part={community[0]}&source=https://www.bayut.com/")
                    else:
                        requests.get(f"http://127.0.0.1:8000/city-prop/?city={city}&part={area[0]}&source=https://www.bayut.com/")
driver.close()




