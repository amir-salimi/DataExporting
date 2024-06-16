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


url = 'https://easymap.ae/our-shop/'
driver = chrome_webdriver()


driver.get(url)

def get_data_each_prj(link):
    driver.get(link)
    find_TR = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_elements(By.TAG_NAME, "tr")
    city = driver.find_element(By.CLASS_NAME, "mkdf-single-product-title").text
    description = driver.find_element(By.ID, "tab-description").text
    figure = driver.find_element(By.CLASS_NAME, "woocommerce-product-gallery__wrapper").find_elements(By.TAG_NAME, "a")

    # get eahc image of prj
    for f in figure:
        img_link = f.get_attribute("href")
        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&img={img_link}")

    input_list = []
    for TR in find_TR:
        input_list.append(TR.find_elements(By.TAG_NAME, "input"))
        
    requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&description={description}")

    try:
        size = input_list[0][0]
        finish = input_list[1][0]
        type = input_list[2][0]
        size.click()
        finish.click()
        type.click()
        size = size.get_attribute("value") 
        finish = finish.get_attribute("value")
        type = type.get_attribute("value")

        price = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text

        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&city={city}&size={size}&finish={finish}&type={type}&price={price}")

    except:
        pass
    #-----------------------------------------------------------------------------------------------------
    try:
        size = input_list[0][1]
        finish = input_list[1][1]
        type = input_list[2][1]
        size.click()
        finish.click()
        type.click()
        size = size.get_attribute("value") 
        finish = finish.get_attribute("value")
        type = type.get_attribute("value")

        price = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&city={city}&size={size}&finish={finish}&type={type}&price={price}")
         
    except:
        pass
    #-----------------------------------------------------------------------------------------------------
    try:
        size = input_list[0][1]
        finish = input_list[1][0]
        type = input_list[2][0]
        size.click()
        finish.click()
        type.click()
 
        price = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
         
        size = size.get_attribute("value") 
        finish = finish.get_attribute("value")
        type = type.get_attribute("value")
         
        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&city={city}&size={size}&finish={finish}&type={type}&price={price}")
    except:
        pass
    #-----------------------------------------------------------------------------------------------------
    try:
        size = input_list[0][0]
        finish = input_list[1][1]
        type = input_list[2][0]
        size.click()
        finish.click()
        type.click()

        price = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text

        size = size.get_attribute("value") 
        finish = finish.get_attribute("value")
        type = type.get_attribute("value")

        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&city={city}&size={size}&finish={finish}&type={type}&price={price}") 
    except:
        pass
    #-----------------------------------------------------------------------------------------------------
    try:
        size = input_list[0][0]
        finish = input_list[1][0]
        type = input_list[2][1]
        size.click()
        finish.click()
        type.click()
 
        price = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        size = size.get_attribute("value") 
        finish = finish.get_attribute("value")
        type = type.get_attribute("value")
        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&city={city}&size={size}&finish={finish}&type={type}&price={price}") 
    except:
        pass
    #-----------------------------------------------------------------------------------------------------
    try:
        size = input_list[0][1]
        finish = input_list[1][1]
        type = input_list[2][0]
        size.click()
        finish.click()
        type.click()
 
        price = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        size = size.get_attribute("value") 
        finish = finish.get_attribute("value")
        type = type.get_attribute("value")
        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&city={city}&size={size}&finish={finish}&type={type}&price={price}")
    except:
        pass
    #-----------------------------------------------------------------------------------------------------
    try:
        size = input_list[0][1]
        finish = input_list[1][0]
        type = input_list[2][1]
        size.click()
        finish.click()
        type.click()
 
        price = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        size = size.get_attribute("value") 
        finish = finish.get_attribute("value")
        type = type.get_attribute("value")
        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&city={city}&size={size}&finish={finish}&type={type}&price={price}")
    except:
        pass
    #-----------------------------------------------------------------------------------------------------
    try:
        size = input_list[0][0]
        finish = input_list[1][1]
        type = input_list[2][1]
        size.click()
        finish.click()
        type.click()
 
        price = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        size = size.get_attribute("value") 
        finish = finish.get_attribute("value")
        type = type.get_attribute("value")
        requests.get(f"http://127.0.0.1:8000/easymap-data/?link={link}&city={city}&size={size}&finish={finish}&type={type}&price={price}")
    except:
        pass


each_prj_link = []

prj = driver.find_element(By.CLASS_NAME, "mkdf-page-content-holder").find_elements(By.CLASS_NAME, "vc_row")
for p in prj:   
    for a in p.find_elements(By.TAG_NAME, "a"):
        if "https://easymap.ae/shop/" in a.get_attribute("href"):
            each_prj_link.append(a.get_attribute("href"))

for i in set(each_prj_link):
    get_data_each_prj(i)



time.sleep(5000)
