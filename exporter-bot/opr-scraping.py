from bs4 import BeautifulSoup
import requests

import time

from help import remove_new_line, split_data, delete_repeat_data


url = "https://opr.ae/projects"

load_more_url = "https://api.opr.ae/offplan/"



def get_each_project_approximate_location(soup):
    data = ""
    try:
        location = soup.find(id="location").find_all(class_="zero-layer")
        for i in location:
            if i.text != "":
                data += i.text + ", "
        return data
    except:
        pass


def get_bed_area_data(soup):
    data_array = []
    try:
        floor_plans = soup.find(id="floor-plans").find_all(class_="swiper-slide")
        for plan in floor_plans:
            data = plan.find('p', class_="textable")
            data = remove_new_line(data.text)
            data_array.append(data)
        s_data = split_data(data_array, ["Total:", "sqft"], ["-BedroomUnit"])
        return s_data
    except:
        try:
            floor_plans = soup.find(id="fp").find_all(class_="swiper-slide")
            for plan in floor_plans:
                data = plan.find('p', class_="textable")
                data = remove_new_line(data.text)
                data_array.append(data)
            s_data = split_data(data_array, ["Total:", "sqft"], ["-BedroomUnit"])
            return s_data
        except:
            pass


def get_each_project_handover(soup):
    array = []
    handover = soup.find_all(class_="zero-layer-frame node-stretch")
    for i in handover:
        if i.text != "":
            data = remove_new_line(i.text)
            array.append(data)
    return split_data(array, ["HANDOVER"], None)
     

def get_eahc_project_plan(soup, link):
    plan_array = []
    plan_data = soup.find_all(class_="swiper-slide")
    for p in plan_data:
        if p.select_one("img") != None:
            plan_array.append(p.select_one("img").get("data-lazy-image"))
    plan_map = delete_repeat_data(plan_array)
    for i in plan_map:
        requests.get(f"http://127.0.0.1:8000/opr_data/?link={link}&plan={i}")



def get_each_project_img(soup, link):
    imgs = soup.find_all(class_='gallery427-image fancybox')
    for img in imgs:
        image = img.get("href")
        requests.get(f"http://127.0.0.1:8000/opr_data/?link={link}&img={image}")



def get_each_project_about(soup, link):
    try:
        about = soup.find(id="about").find(class_="node").find_all(class_="col")
        for i in about:
            data = remove_new_line(i.text)
            requests.get(f"http://127.0.0.1:8000/opr_data/?about={data}&link={link}")
    except:
        pass

def get_each_project_frequently_question(soup, link):
    array = []
    try:
        question = soup.find(id="questions-and-answers").find_all(class_="node")
        for q in question:
            data = q.text
            data = data.replace("\n", "")
            array.append(data)  
        for i in array:
            if i[::-1][:1] == "?":
                requests.get(f"http://127.0.0.1:8000/opr_data/?question={i}&answer={array[array.index(i)+1]}&link={link}")
    except:
        pass

def get_data_from_each_link(link, array):
    each_page = requests.get(link)
    each_soup = BeautifulSoup(each_page.content, "html.parser")

    get_each_project_about(each_soup, link)

    get_each_project_frequently_question(each_soup, link)

    get_each_project_img(each_soup, link)

    get_eahc_project_plan(each_soup, link)

    bed_area = get_bed_area_data(each_soup)
    
    handover = get_each_project_handover(each_soup)

    approximate_location = get_each_project_approximate_location(each_soup)
    try:
        for i in range(len(bed_area[0])):    
            bed_room = bed_area[1][i]
            area = bed_area[0][i]
            area = area.replace(",", "")
            HANDOVER = handover[0][0]
            name = array[0]
            location = array[1]
            developer = array[2]
            category = array[4]
            price = array[5]
            payment_plan = array[6]
            status = array[7]
            requests.get(f"http://127.0.0.1:8000/opr_data/?bed_room={bed_room}&handover={HANDOVER}&area={area}&name={name}&location={location}&developer={developer}&category={category}&link={link}&approximate_location={approximate_location}&price={price}&payment_plan={payment_plan}&status={status}")

    except:
        pass
    

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
    
    array = [name, location, developer, link, category, price, payment_plan, status]
    value = get_data_from_each_link(link, array)
    
    


def load_another_page():
    for i in range(2, 28):
        loaded_page = requests.post(load_more_url, data={"page":f"{i}", "action":"getList", "language":"EN"})
        loaded_soup = BeautifulSoup(loaded_page.content, "html.parser")
        all_loaded_data = loaded_soup.find_all(class_="offPlanListing__item")
        for soup in all_loaded_data:
            time.sleep(1)
            val = get_detail(soup)
        print(i)

            
            

def first_page_data():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    all_data = soup.find_all(class_="offPlanListing__item")
    for soup in all_data:
        val = get_detail(soup)
    load_another_page()



first_page_data()




