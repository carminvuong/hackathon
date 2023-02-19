import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint


url = 'https://www.careerjet.com/jobad/us827927d1693748b79497a7207bcc7230'


def getDescription(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    html = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()

    return str(html.find_all('section', class_='content'))


getDescription(url)
