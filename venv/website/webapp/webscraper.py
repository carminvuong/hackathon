import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import lxml
import cchardet


url = 'https://www.careerjet.com/jobad/us827927d1693748b79497a7207bcc7230'


def getSeeMore(url):
    driver = webdriver.Chrome()

    driver.get(url)
    driver.execute_script("window.stop();")
    html = BeautifulSoup(driver.page_source, 'lxml')
    words = html.find_all('div', class_='desc')
    lst = []
    for i in words:
        lst.append(i.get_text(strip=True))
    return lst


def getDescription(url):
    driver = webdriver.Chrome()

    driver.get(url)
    driver.execute_script("window.stop();")
    html = BeautifulSoup(driver.page_source, 'lxml')
    words = html.find_all('section', class_='content')
    return words[0]
