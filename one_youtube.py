from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import localtime, strftime

path = "chromedriver"
driver = webdriver.Chrome(path)
driver.get('https://www.youtube.com/playlist?list=PLU12uITxBEPGpEPrYAxJvNDP6Ugx2jmUx')

page = driver.page_source
soup = BeautifulSoup(page,'html.parser')
driver.find_element_by_xpath('//*[@id="contents"]/ytd-playlist-video-renderer[1]').click()
#driver.find_element_by_css_selector('#contents > ytd-playlist-video-renderer:nth-child(1)').click()

page = driver.page_source
soup = BeautifulSoup(page,'html.parser')

all_view_num = soup.find_all('span','view-count style-scope yt-view-count-renderer')
view_num = [soup.find_all('span','view-count style-scope yt-view-count-renderer')[n].string for n in range(0,len(all_view_num))]
view_numm




