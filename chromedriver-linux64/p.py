from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

import time

import pickle

cookie = {
    "G_ENABLED_IDPS" : "google" ,
    "IS_AUTH" : "Y",
    "NEW_USER" : "N", 
    "PROP_TREND" : "ORA_WWV-yhgCaAbNpJZrphMeQbVhDLph",
    "USEREMAIL" : "amir0905salimi@gmail.com", 
    "cf_clearance" : "1u17qSV044UJZc0c_kOrKj9u7J1GzBuEGZPfN1y8A_4-1716886853-1.0.1.1-CnD9ETaFaNroNDtNRLNg4lvp94iUREwfc3wMmSe3_66TNUf0oqKibE8SyKKg1POKiaWmi7lOVMcIIfwVp8aIEg",
}

def chrome_webdriver():
    chromedriver_path = '/home/amir/Documents/export_data/chromedriver-linux64/chromedriver'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/123.0.0.0 Safari/537.36'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    options.add_argument(f'user-agent={user_agent}')
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def javascript_apex_converter(data):
    array = []
    data = data[31:-1]
    data = data.replace("u0026", "&").split(",")
    for i in data:
        array.append(i)
    data = array[0]
    data = data[60:-1]
    data = data.replace("\\", "")
    link = "https://dxbinteract.com/r/property/trends/transaction-details?" + data
    print(link)
    # get_each_link_data(data)

# import requests
# def get_each_link_data(data):
#     driver.get(data)
#     driver.find_element
#     ...

# def get_all_data(page):
#     soup = BeautifulSoup(page, "html.parser")
#     all_sold_prj = soup.find(id="soldhistory").find(class_="t-Report-tableWrap").find("tbody").find_all("tr")

#     for i in all_sold_prj:
#         link = i.select_one("a").get("href")
#         javascript_apex_converter(link)         




url = 'https://dxbinteract.com/'
driver = chrome_webdriver()
print("1")
a = driver.get(url)
print("1")

for key, value in cookie.items():
    print(key, value)
    driver.add_cookie({"name": key, "value" : value})

driver.get("https://dxbinteract.com/dubai-house-prices")

a = driver.find_element(By.ID, "soldhistory").find_element(By.CLASS_NAME, "t-Report-tableWrap").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")


for i in a:
    data = i.find_element(By.TAG_NAME, "a").get_attribute("href")
    driver.execute_script(data)
    time.sleep(5)
    # data = i.find_element(By.TAG_NAME, "a").get_attribute("href")
    # javascript_apex_converter(data)





time.sleep(5000)
