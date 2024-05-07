from bs4 import BeautifulSoup
import requests
import time
import html_to_json
import re


url = "https://opr.ae/projects"

load_more_url = "https://api.opr.ae/offplan/"

max_page = 27


def remove_new_line(data):
    data = data.replace("\n", "")
    data = data.replace(" ", "")
    return data


def delete_repeat_data(array):
    new_array = list(set(array))

    return new_array


def get_data_from_each_link(link, array):
    plan_array = []
    each_page = requests.get(link)
    each_soup = BeautifulSoup(each_page.content, "html.parser")

    img = each_soup.find_all(class_='gallery427-image fancybox')
    
    plan_data = each_soup.find_all(class_="swiper-slide")
    
    for p in plan_data:
        if p.select_one("img") != None:
            plan_array.append(p.select_one("img").get("data-lazy-image"))

    plan_map = delete_repeat_data(plan_array)

    for i in img:
        each_img = i.get("href")
        
    for i in each_soup.find_all(class_="tabs3-page"):
        array = array
        if "Bedroom" in i.text:
            bed = remove_new_line(i.text)
    
    
    print("------------------------------------------------------------------------------------------------")
    
        



def get_detail(soup):
    array = []
    name = soup.find(class_="offPlanListing__item-titleLink").text
    location = soup.find(class_="offPlanListing__item-locations").text
    developer = soup.find(class_="offPlanListing__item-developer").text
    link = soup.find(class_="offPlanListing__item-blockLink").get("href")
    category = soup.find(class_="offPlanListing__item-type").text
    try:
        price = soup.find(class_="offPlanListing__item-price").select_one("span").get("data-price")
    except:
        price = "Ask for"
    try:
        payment_plan = soup.find(class_="offPlanListing__stickers-item red").text
    except:
        payment_plan = None
    try:
        status = soup.find(class_="offPlanListing__stickers-item green").text
    except:
        status = None
    
    array = [name, location, developer, link, category]
    value = get_data_from_each_link(link, array)
    
    


def load_another_page():
    for i in range(2, 28):
        loaded_page = requests.post(load_more_url, data={"page":f"{i}", "action":"getList", "language":"EN"})
        loaded_soup = BeautifulSoup(loaded_page.content, "html.parser")
        all_loaded_data = loaded_soup.find_all(class_="offPlanListing__item")
        for soup in all_loaded_data:
            val = get_detail(soup)

            
            

def first_page_data():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    all_data = soup.find_all(class_="offPlanListing__item")
    for soup in all_data:
        val = get_detail(soup)
    print("***********************************************************************************************************")
    load_another_page()



first_page_data()




