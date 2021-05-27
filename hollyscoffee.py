from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

result = []

for page in range(1,30):
    Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
    html = urllib.request.urlopen(Hollys_url)
    soupHollys = BeautifulSoup(html, 'html.parser')
    tag_tbody = soupHollys.find('tbody')
    for store in tag_tbody.find_all('tr'):
        if len(store) <= 3:
            break
        store_td = store.find_all('td')

        store_name = store_td[1].string
        print("지점명 : ", store_name)
        store_sido = store_td[0].string
        print("지역 : ", store_sido)
        store_address = store_td[3].string
        print("주소 : ", store_address)
        store_phone = store_td[5].string
        print("폰번호 : ", store_phone)
        result.append([store_name]+[store_sido]+[store_address]+[store_phone])


hollys_tbl = pd.DataFrame(result, columns = ('store', 'sido-gu', 'address', 'phone'))
hollys_tbl.to_csv("C:/My_Python/kroling/hollyscoffee.csv", encoding = "cp949", mode = "w", index = True)