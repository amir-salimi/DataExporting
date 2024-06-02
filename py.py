import requests
from urllib3 import request

# from selenium import webdriver

from bs4 import BeautifulSoup
import json

#turn post string into dict: 
def parsePOSTstring(POSTstr):
    paramList = POSTstr.split('&')
    paramDict = dict([param.split('=') for param in paramList])
    return paramDict

# this is my user cookies
cookie = {
    "G_ENABLED_IDPS" : "google" ,
    "IS_AUTH" : "Y",
    "NEW_USER" : "N", 
    "PROP_TREND" : "ORA_WWV-_gUisEKwwaQVTd1KfONgjHzI",
    "USEREMAIL" : "amir0905salimi@gmail.com", 
    "cf_clearance" : "NayC3lNdtPeb8inc_qh0bgvEiqUDTCdWaujG_4WjtFE-1716371794-1.0.1.1-94WRwG9F2WaIjcSTf1nIgH6R6NZE6u4SrBx8vfvVHvGn_rGk61oLvgirQ8J0_z4pb1NwgH15l0fp3X_RqZs_4A"	,
}

# convert the apex javascript to url
def javascript_apex_converter(data):
    array = []
    data = data[31:-1]
    data = data.replace("u0026", "&").split(",")
    for i in data:
        array.append(i)
    data = array[0]
    data = data[60:-1]
    data = data.replace("\\", "")
    print("https://dxbinteract.com/r/property/trends/transaction-details?" + data)


def get_data(page):
    soup = BeautifulSoup(page.content, "html.parser")
    all_sold_prj = soup.find(id="soldhistory").find("tbody")
    a = all_sold_prj.find_all("tr")
    for i in a:
        link = i.select_one("a").get("href")
        javascript_apex_converter(link)                                                                                                                                                                                                                                                                                     



s = requests.Session()
url = 'https://dxbinteract.com/'

import time

while True:

    res = requests.get(url)
    # res = request("GET", "https://dxbinteract.com/", headers=headers)
    print(res)

    # page = requests.post("https://dxbinteract.com/wwv_flow.ajax?p_context=trends/sales-rent-property-prices/6047562163019", headers=header, cookies=dict(cookie))
    # print(page) 
    # print(page.cookies)
    # if page.status_code == 200:
    #     # get_data(page)
    #     break




