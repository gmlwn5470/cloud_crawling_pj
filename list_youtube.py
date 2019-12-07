from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import localtime, strftime
import time
import csv

path = "chromedriver"
driver = webdriver.Chrome(path)

for count in range(1,7):
    driver.get('https://www.youtube.com/playlist?list=PLU12uITxBEPGpEPrYAxJvNDP6Ugx2jmUx')

    total_list = []
    j=2
    for i in range(1,21):
        #driver.find_element_by_css_selector('#contents > ytd-playlist-video-renderer:nth-child('+str(i)+')').click()
        driver.find_element_by_xpath('//*[@id="contents"]/ytd-playlist-video-renderer['+str(i)+']').click()
    #contents > ytd-playlist-video-renderer:nth-child(6)
    #여기서부터

        body = driver.find_element_by_tag_name('body')
        num_of_pagedowns = 4
        #10번 밑으로 내리는 것
        while num_of_pagedowns:
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            num_of_pagedowns -= 2
        #여기까지
  
        page = driver.page_source
        soup = BeautifulSoup(page,'html.parser')

        all_chennel = soup.find_all('a','yt-simple-endpoint style-scope yt-formatted-string')
        chennel = [soup.find_all('a','yt-simple-endpoint style-scope yt-formatted-string')[n].string for n in range(0,len(all_chennel))]

        all_view_num = soup.find_all('span','view-count style-scope yt-view-count-renderer')
        view_num = [soup.find_all('span','view-count style-scope yt-view-count-renderer')[n].string for n in range(0,len(all_view_num))]

        extract_date = strftime("%Y/%m/%d %H:%M:%S", localtime())

        youtube_video_list = []
    
        for i in range(0,len(all_view_num)):
            roww = []
            roww.append(chennel[j])
            roww.append(view_num[i])
            roww.append(extract_date)
            youtube_video_list.append(roww)
        
        total_list += youtube_video_list
        j +=1
        driver.back()
    
        element=driver.find_element_by_tag_name('html')
        for i in range(2): 
            element.send_keys(Keys.ARROW_DOWN)
            time.sleep(3)
        
#total_list
    time_ = strftime("%m%d_%H%M%S", localtime())
    csvfile = open("Desktop/%s.csv" %time_,"w",-1,"utf-8")
#csvfile = open("Desktop/test%d.csv" % k ,"w",-1,"utf-8")
#k += 1;
    csvwriter = csv.writer(csvfile)
    for row in total_list:
        csvwriter.writerow(row)
    csvfile.close()

    time.sleep(1200)
