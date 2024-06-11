from bs4 import BeautifulSoup

from help import remove_new_line

import requests
import time


dxb_url = "https://dxboffplan.com/offplan-projects/"



def data_from_url(link_array):

    data_array = []

    for link in link_array:
        each_page = requests.get(link)
        each_soup = BeautifulSoup(each_page.content, "html.parser")

        if each_page.status_code == 429:
            time.sleep(3)

        name = each_soup.find(class_="single-property-title").text
        all_data = each_soup.find_all(class_="s-cl")
        development = each_soup.find("p", class_="development").text
        city = each_soup.find("p", class_="city").text
        img = each_soup.find(class_="head-img").select_one("img").get('src')

        for data in all_data:
            val = remove_new_line(data.text)
            data_array.append(val)
        
        price = data_array[0].replace(",", "")
        price_per_meter = data_array[1].replace(",", "")

        area = remove_new_line(data_array[2])
        location = data_array[5]
        developer = data_array[6]
        developer_project_number = data_array[7]
        handover = data_array[8]
        views = data_array[9]
        category = data_array[3]
        bed_room = data_array[4]
        bed_room = bed_room.split(".")
        for bed in bed_room:
                requests.get(f"http://127.0.0.1:8000/dxb-data/?name={name}&development={development}&city={city}&img={img}&price={price}&price_per_meter={price_per_meter}&area={area}&category={category}&bed_room={bed}&views={views}&handover={handover}&developer_project_number={developer_project_number}&developer={developer}&location={location}&link={link}")


        data_array = []
    return 

def get_link():
    link_array = []
    page = requests.post(dxb_url, data={"page":"10"})
    soup = BeautifulSoup(page.content, "html.parser")
    for adv in soup.find_all(class_="card property-card"):
        link = adv.select_one('a').get("href")
        link_array.append(link)

    data_from_url(link_array)


get_link()
