import webbrowser as web
import time

url = 'www.google.com'

def chrome(url):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    google= web.get(chrome_path)
    google.open(url)

def explore(url):
    ie= web.get(web.iexplore)
    ie.open(url)

import urllib.request
from time import time

def aa():
    url = 'www.google.com'
    explore='C:/Program Files (x86)/Internet Explorer/iexplore.exe %s'
    stream= web.get(explore)
    start_time = time()
    stream.open(url)
    end_time = time()

    print(end_time-start_time)
    print("aa",round(end_time-start_time, 3))
#aa()

def bb():
    url = 'www.google.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    stream= web.get(chrome_path)
    dizi=[]
    for i in range(10):
        start_time = time()
        stream.open(url)
        end_time = time()
        dizi.append(round(end_time-start_time, 3))
    print(dizi)

import time
from selenium import webdriver
def ddd():
    driver = webdriver.Chrome(executable_path=r"C:\Users\Engin\PycharmProjects\untitled\Yazılım Kalite\chromedriver.exe")
    start = time.time()
    driver.get('http://stackoverflow.com')
    end = time.time()
    print(end - start)
    driver.quit()
ddd()