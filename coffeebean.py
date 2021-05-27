from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time

#커피빈 매장정보 동적 크롤링
#storePop2()스크립트에 매장번호를 넣어서 동적으로 매장 정보를 받아온다.
# 1. 매장이름, 2. 주소, 3. 전화번호

# 준비 
# 1. selenium 라이브러리 설치 ( pip install selenium )
# 2. webdriver 다운로드 {주의 : 크롬버전과 같은 버전으로 다운} 
#    (https://chromedriver.chromium.org/downloads)


#[CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp" 
    wd = webdriver.Chrome('./chromedriver.exe')

    for i in range(1, 300): #매장 수만큼 반복하기
        wd.get(CoffeeBean_URL)
        time.sleep(0.5) #웹페이지 연결할 동안 1초 대기
        try:
            wd.execute_script("storePop2(%d)" %i)
            time.sleep(0.5) #스크립트 실행할 동안 1초 대기
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            # 매장이름
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            print(store_name) #매장 이름 출력하기
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            # 주소
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            # 전화번호
            store_phone = store_info[3].string
            # result배열에 추가
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
    return

#[CODE 0]
def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result) #[CODE 1]

    # pandas의 dataframe함수로 테이블 만들기
    CB_tbl = pd.DataFrame(result, columns = ('store', 'address','phone'))
    # 만든 테이블 csv로 저장
    CB_tbl.to_csv('./CoffeeBean.csv', encoding = 'cp949', mode = 'w', index = True)

if __name__ == '__main__':
    main()