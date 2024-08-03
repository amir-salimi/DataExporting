from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import os, time, requests, sqlite3, json


def chrome_webdriver():
    chromedriver_path = os.getcwd()+"/chromedriver"
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    options.add_argument(f'user-agent={user_agent}')
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


driver = chrome_webdriver()
connection = sqlite3.connect("/home/amir/Documents/export_data/core/db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT * FROM buildings")
data = cursor.fetchall()


def get_agency_bio(agency_bio_link):
    agency_details_list = []
    prop_types = None        
    service_areas = None        
    properties = None
    description = None
    brn = None
    arra = None
    ded = None

    headers = {
        'Content-Type': 'application/json'
    }   

    driver.get(agency_bio_link)

    agency_name = driver.find_element(By.XPATH, "//*[@aria-label='Agency name']").text
    agency_img = driver.find_element(By.XPATH, f"//*[@aria-label='Agency logo']").get_attribute("src")
    
    driver.find_element(By.XPATH, "//span[text()='Read all']").click()
    try:
        driver.find_element(By.XPATH, "//span[text()='See all areas']").click()
    except:
        pass

    time.sleep(5)
    agency_details = driver.find_elements(By.XPATH, "//div[@dir='ltr']")
    
    for detail in agency_details:
        agency_detail = detail.text
        if "Read less" in agency_detail:
            agency_detail = agency_detail.replace("Read less", "")
        if "See less areas" in agency_detail:
            agency_detail = agency_detail.replace("See less areas", "")

        agency_detail = agency_detail.replace("&", "and").replace("'", "")
        agency_details_list.append(agency_detail)


    if "Description" in str(agency_details_list): # if the data is not complite it restart the function with agent_bio_link
        pass
    else:
        get_agency_bio(agency_bio_link)

    driver.find_element(By.XPATH, "//button[@aria-label='Call']").click()

    time.sleep(3)

    agency_phone_number = driver.find_element(By.XPATH, "//*[@aria-label='Listing phone number']").text

    for detail in agency_details_list:
        if "Property Types" in detail:
            prop_types = detail.split(":")
            prop_types = prop_types[1]
        if "Service Areas" in detail:
            service_areas = detail.split(":")
            service_areas = service_areas[1]
        if "Properties" in detail:
            properties = detail.split(":")
            properties = properties[1]
        if "Description" in detail:
            description = detail.split(":")
            description = description[1] 
        if "BRN" in detail:
            brn = detail.split(":")
            brn = brn[1] 
            brn = brn.replace("\n", "")
        if "ARRA" in detail:
            arra = detail.split(":")
            arra = arra[1] 
            arra = arra.replace("\n", "")
        if "DED" in detail:
            ded = detail.split(":")
            ded = ded[1] 
            ded = ded.replace("\n", "")   


    post_data = {
        "name": str(agency_name),
        "photo": str(agency_img),
        "link": str(agency_bio_link),
        "property_types": str(prop_types),
        "service_areas": str(service_areas),
        "properties": str(properties),
        "description": str(description),
        "brn": str(brn),
        "arra": str(arra),
        "ded": str(ded),
        "phone_number": str(agency_phone_number)
    }
    requests.post(url="http://127.0.0.1:8000/agency/", data=json.dumps(post_data), headers=headers)


def get_agent_bio(agent_bio_link):
    agent_details_list = []
    languages = None
    specialities = None
    service_areas = None
    properties = None
    description = None
    brn = None
    experience = None

    headers = {
        'Content-Type': 'application/json'
    } 

    driver.get(agent_bio_link)

    agency_name = driver.find_element(By.XPATH, "//*[@aria-label='Agency name']").text
    agency_bio_link = driver.find_element(By.XPATH, "//*[@aria-label='Agency name']").find_element(By.TAG_NAME, "a").get_attribute("href")
    get_agency_bio(agency_bio_link)

    driver.get(agent_bio_link)

    agent_name = driver.find_element(By.XPATH, "//*[@aria-label='Agent name']").text
    try:
        agent_img = driver.find_element(By.XPATH, f"//*[@aria-label='Agent {agent_name}']").get_attribute("src")
    except:
        agent_img = None

    driver.find_element(By.XPATH, "//span[text()='Read all']").click()    
    try:
        driver.find_element(By.XPATH, "//span[text()='See all areas']").click()
    except:
        pass
    time.sleep(5)

    agent_details = driver.find_elements(By.XPATH, "//div[@dir='ltr']")

    driver.find_element(By.XPATH, "//*[@aria-label='Call']").click()
    time.sleep(3)
    agent_phone_number = driver.find_element(By.XPATH, "//*[@aria-label='Listing phone number']").text
    
    for detail in agent_details:
        agent_detail = detail.text
        if "Read less" in agent_detail:
            agent_detail = agent_detail.replace('Read less', '')
        if "BRN" in agent_detail:
            agent_detail = agent_detail.replace('\n', '')
        agent_detail = agent_detail.replace("&", "and")
        agent_details_list.append(agent_detail)

    newList = [item.replace("'", '"') for item in agent_details_list]

    for detail in newList:
        if "Language(s)" in detail:
            languages = detail.split(":")
            languages = languages[1]
        if "Specialities" in detail:
            specialities = detail.split(":")
            specialities = specialities[1]
        if "Service Areas" in detail:
            service_areas = detail.split(":")
            service_areas = service_areas[1]
        if "Properties" in detail:
            properties = detail.split(":")
            properties = properties[1]
        if "Description" in detail:
            description = detail.split(":")
            description = description[1] 
        if "BRN" in detail:
            brn = detail.split(":")
            brn = brn[1] 
        if "Experience" in detail:
            experience = detail.split(":")
            experience = experience[1]     
    
    post_data = {
        "name": agent_name,
        "link": agent_bio_link,
        "photo": agent_img,
        "languages": languages,
        "specialities": specialities,
        "service_areas": service_areas,
        "properties": properties,
        "description": description,
        "experience": experience,
        "phone_number": agent_phone_number,
        "brn": brn,
        "agency": agency_name
    }
    requests.post(url="http://127.0.0.1:8000/agent/", data=json.dumps(post_data), headers=headers)
  

def get_each_prop_detail(all_link, building_name):
    headers = {
        'Content-Type': 'application/json'
    } 

    for link in all_link:
            complex = None
            agency_bio_link = None
            driver.get(link)
            price = driver.find_element(By.XPATH, "//*[@aria-label='Price']").text
            location = driver.find_element(By.XPATH, "//*[@aria-label='Property header']").text
            bed = driver.find_element(By.XPATH, "//*[@aria-label='Beds']").text
            bath = driver.find_element(By.XPATH, "//*[@aria-label='Baths']").text
            unit_area = driver.find_element(By.XPATH, "//*[@aria-label='Area']").text
            price = driver.find_element(By.XPATH, "//*[@aria-label='Price']").text
            desc = driver.find_element(By.XPATH, "//*[@aria-label='Property description']").text
            location = location.split(",")

            agent_bio_link = driver.find_element(By.XPATH, "//*[@aria-label='Agent name']").get_attribute("href")
            if agent_bio_link is None:
                agency_bio_link = driver.find_element(By.XPATH, "//*[@aria-label='View all properties']").get_attribute("href")
                
    

            if len(location) == 5:
                name = location[0]
                complex = location[1]
                community = location[2]
                area = location[3]
                city = location[4]

            elif len(location) == 4:
                name = location[0]
                community = location[1]
                area = location[2]
                city = location[3]

            elif len(location) == 3:
                name = location[0]
                area = location[1]
                city = location[2]
                community = None
            
            else:
                name = None
                area = None
                city = None
                community = None
                complex = None

            if name != None:
                if name[0] == " ":
                    name = name[1:]
            if complex != None:
                
                if complex[0] == " ":
                    complex = complex[1:]

            if community != None:
                if community[0] == " ":
                    community = community[1:]

            if area != None:
                if area[0] == " ":
                    area = area[1:]

            if city != None:
                if city[0] == " ":
                    city = city[1:]
       

            prop_detials = driver.find_element(By.XPATH, "//*[@aria-label='Property details']").find_elements(By.TAG_NAME, "li")

            for prop_detail in prop_detials:
                prop_detail = prop_detail.text.split("\n")
                key = prop_detail[0]
                value = prop_detail[1]

                requests.post(
                    url="http://127.0.0.1:8000/unit-detail/",
                    data=json.dumps(
                        {
                            "building_link": link,
                            "key": key,
                            "value": value
                        }
                    ),
                    headers=headers
                )

            time.sleep(3)
            driver.find_element(By.XPATH, "//*[@aria-label='View gallery']").click() # opening photos window
            photos = driver.find_element(By.XPATH, "//*[@aria-label='Gallery dialog photo grid']").find_elements(By.TAG_NAME, "img")

            for photo in photos:
                photo = photo.get_attribute("src")
                
                requests.post(
                    url="http://127.0.0.1:8000/unit-photo/",
                    data=json.dumps(
                        {
                            "building_link": link,
                            "img_link": photo
                        }
                    ),
                    headers=headers
                )
    
            try:
                get_agent_bio(agent_bio_link)
            except:
                get_agency_bio(agency_bio_link)


            post_data = json.dumps(
                {
                    "building_name": str(building_name),
                    "bed": str(bed),
                    "bath": str(bath),
                    "area": str(area),
                    "description": str(desc),
                    "building_link": str(link),
                    "price": str(price),
                    "agent": str(agent_bio_link),
                    "agency": str(agency_bio_link)
                }
            )
            if building_name and area and city is not None:
                req = requests.post(url="http://127.0.0.1:8000/unit/", headers=headers, data=post_data)
                if req.status_code == 500:
                    req = requests.post(url="http://127.0.0.1:8000/unit/", headers=headers, data=post_data)
    

           
def get_each_prop(building_name):
    all_link = []
    time.sleep(5)
    
    a = driver.find_elements(By.XPATH, "//*[@aria-label='Listing']")
    for n in a:
        link = n.find_element(By.TAG_NAME, "a").get_attribute("href")
        all_link.append(link)

    while True:
        try:
            driver.find_element(By.XPATH, "//*[@title='Next']").click()
            a = driver.find_elements(By.XPATH, "//*[@aria-label='Listing']")
            time.sleep(8)
            for n in a:
                link = n.find_element(By.TAG_NAME, "a").get_attribute("href")
                all_link.append(link)
        except:
            break
    get_each_prop_detail(all_link, building_name)


def go_to_search_input(search_input):
    driver.get("https://www.bayut.com/")
    input = driver.find_element(By.XPATH, "//*[@placeholder='Enter location']")
    input.send_keys(f"{search_input}")
    time.sleep(4)
    input.send_keys(Keys.SPACE)
    time.sleep(10)
    input.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@aria-label='Find button']").click()
    time.sleep(1)


for i in data:
    if i[7] == 1:
        go_to_search_input(i[1])
        get_each_prop(i[1])


