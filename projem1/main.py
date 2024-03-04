from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import random

with open('beyza.txt', 'r', encoding='utf-8') as messages:
    messagelist = list()
    text = messages.read()
    messagelist = text.split('\n')

flag = False

def start():
    driver_path = r"C:\Users\beyza\OneDrive\Masaüstü\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com/')
    input("QR kodu okuttuysanız bir tuşa basıp enterlayın.")

    while True:
        try:
            message_area = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
        except:
            time.sleep(2)
            continue

        message_area.click()
        wp_source = driver.page_source
        soup = bs(wp_source, 'html.parser')
        search = soup.find_all('div', {'class': ['p357zi0d r15c9g6i g4oj0cdv ovllcyds l0vqccxk pm5hny62','ggj6brxn gfz4du6o r7fjleex lhj4utae le5p0ye3 _11JPr selectable-text copyable-text']})
        try:
            online = search[0].span.text
            print(online)
            if (online in ['çevrimiçi', 'online']) and not flag:
                print('online')
                msgToSend = messagelist[random.randint(0, len(messagelist) - 1)]
                message_area.send_keys(msgToSend)
                message_area.send_keys(Keys.ENTER)
                flag = True
            elif online not in ['çevrimiçi', 'online']:
                print('Şu an da çevrimdışı')
                flag = False
        except IndexError:
            print('Şu an da çevrimdışı')
            flag = False

        time.sleep(5)

start()
