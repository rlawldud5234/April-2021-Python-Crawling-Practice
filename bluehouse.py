from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import time
import pandas as pd

baseUrl = 'https://www1.president.go.kr/petitions/?c=47&only=1&page=1&order=1'
driver = webdriver.Chrome()
driver.get(baseUrl)
SCROLL_PAUSE_TIME=1 #동적 페이지의 로딩을 기다리기 위한 상수 (1초)

n = 0 #데이터의 갯수
result =[]

last_height = 0 #무한스크롤을 위해 창의 높이를 저장
for page in range(1,14):

    while True:
        # 화면 최하단으로 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 페이지 로드를 기다림
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
        
        time.sleep(SCROLL_PAUSE_TIME)

        #새로운 창 높이를 가져온다.
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 스크롤 종료 크롤링 시작
        if new_height == last_height:
            
            #li태그들 가져오기
            li=driver.find_elements_by_css_selector("ul.petition_list > li")
            for i in li:
                #번호
                article_no = i.find_element_by_class_name('bl_no').text
                print("번호",article_no)
                #제목
                article_name = i.find_element_by_class_name('bl_subject').text
                print("제목",article_name)
                # #청원 종료일
                article_date = i.find_element_by_class_name('bl_date').text
                print("청원종료일",article_date)
                # #참여인원
                article_agree = i.find_element_by_class_name('bl_agree').text
                print("참여인원",article_agree)
                result.append([article_no]+[article_name]+[article_date]+[article_agree])
                
            blue_url = 'https://www1.president.go.kr/petitions/?c=47&only=1&page=%d&order=1' %page
            driver.get(blue_url)
            break
        
        # 스크롤 다운되고 새로운 창 높이를 지난 창 높이로 갱신
        last_height = new_height

# pandas의 dataframe함수로 테이블 만들기
p1_tbl = pd.DataFrame(result, columns = ('number', 'title','date','agree'))
# 만든 테이블 csv로 저장
p1_tbl.to_csv('./bluehouse.csv', encoding = 'cp949', mode = 'w', index = True)