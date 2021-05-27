from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import time


plusUrl = input('검색어 입력: ')
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
url = baseUrl+plusUrl
driver = webdriver.Chrome()
driver.get(url)
SCROLL_PAUSE_TIME=2 #동적 페이지의 로딩을 기다리기 위한 상수 (2초)

n = 0 #데이터의 갯수

last_height = 0 #무한스크롤을 위해 창의 높이를 저장

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
        #이미지 태그들 가져오기
        img=driver.find_elements_by_css_selector("div.photo_bx > div.thumb > a > img")
        for i in img:
            print(n)

            src=i.get_attribute('src')
            if(src[:5]!="https"): #이미지가 아닌것을 검출(https로 시작하는게 아니면 넘기기)
                print(False)
                continue
            with urlopen(src) as f: #이미지 저장
                with open('./img/taycan'+str(n)+'.jpg','wb') as h:
                    image= f.read()
                    h.write(image)
            print(src)
            n +=1
        break
    
    # 스크롤 다운되고 새로운 창 높이를 지난 창 높이로 갱신
    last_height = new_height



# driver.implicitly_wait(10) 


