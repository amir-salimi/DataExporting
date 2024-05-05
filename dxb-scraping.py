from bs4 import BeautifulSoup

import requests
import time


dxb_url = "https://dxboffplan.com/fa/offplan-projects/"



def data_from_url(link_array):

    data_array = []

    for link in link_array:
        each_page = requests.get(link)
        each_soup = BeautifulSoup(each_page.content, "html.parser")

        if each_page.status_code == 429:
            time.sleep(3)

        # there are the information of each adv page
        all_data = each_soup.find_all(class_="s-cl")
        development = each_soup.find("p", class_="development").text
        city = each_soup.find("p", class_="city").text

        for data in all_data:
            
            data_array.append(data.text)

        data_array.append(development)
        data_array.append(city)
        

        # requests.get(
        #     f"0.0.0.0:8000/?price={data_array[0]}&per_meter_price={data_array[1]}&area={data_array[2]}&category={data_array[3]}&bed_room={data_array[4]}&location={data_array[5]}&developer={data_array[6]}&developer_projects={data_array[7]}&delivery={data_array[8]}&views={data_array[9]}&city={data_array[10]}&development={data_array[11]}"
        # )

        # print("---------------")
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
