from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

import time


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


url = 'https://easymap.ae/our-shop/'
driver = chrome_webdriver()



driver.get(url)

def get_data_each_prj(link):
    
    driver.get(link)
    find_TR = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_elements(By.TAG_NAME, "tr")
    city = driver.find_element(By.CLASS_NAME, "mkdf-single-product-title").text
    description = driver.find_element(By.ID, "tab-description").text
    additional_info_P_tag = driver.find_element(By.ID, "tab-additional-information").find_elements(By.TAG_NAME, "p")
    additional_info_UL_tag = driver.find_element(By.ID, "tab-additional-information").find_elements(By.TAG_NAME, "ul")
    figure = driver.find_element(By.CLASS_NAME, "woocommerce-product-gallery__wrapper").find_elements(By.TAG_NAME, "a")
    print(link)
    for f in figure:
        print(f.get_attribute("href"))
    print(city)
    print(description)
    input_list = []
    for TR in find_TR:
        input_list.append(TR.find_elements(By.TAG_NAME, "input"))
    try:
        size = input_list[0][0]
        finish = input_list[1][0]
        type = input_list[2][0]
        size.click()
        finish.click()
        type.click()
        print(size.get_attribute("value"))
        print(finish.get_attribute("value"))
        print(type.get_attribute("value"))
        price_class = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        print(price_class)
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
        print(size.get_attribute("value"))
        print(finish.get_attribute("value"))
        print(type.get_attribute("value"))
        price_class = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        print(price_class)
         
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
        print(size.get_attribute("value"))
        print(finish.get_attribute("value"))
        print(type.get_attribute("value"))
        price_class = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        print(price_class)
         
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
        print(size.get_attribute("value"))
        print(finish.get_attribute("value"))
        print(type.get_attribute("value"))
        price_class = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        print(price_class)
         
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
        print(size.get_attribute("value"))
        print(finish.get_attribute("value"))
        print(type.get_attribute("value"))
        price_class = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        print(price_class)
         
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
        print(size.get_attribute("value"))
        print(finish.get_attribute("value"))
        print(type.get_attribute("value"))
        price_class = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        print(price_class)
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
        print(size.get_attribute("value"))
        print(finish.get_attribute("value"))
        print(type.get_attribute("value"))
        price_class = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        print(price_class)
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
        print(size.get_attribute("value"))
        print(finish.get_attribute("value"))
        print(type.get_attribute("value"))
        price_class = driver.find_element(By.CLASS_NAME, "mkdf-single-product-summary").find_element(By.CLASS_NAME, "single_variation_wrap").find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        print(price_class)
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
