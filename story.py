from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import pandas as pd

result=[]
#https://www1.president.go.kr/petitions/?c=47&only=1&page=1&order=1
#https://www1.president.go.kr/petitions/?c=47&only=1&page=14&order=1
#교통/건축/국토 목록
#url open

for page in range(1,14):
    blue_url = 'https://www1.president.go.kr/petitions/?c=47&only=1&page=%d&order=1' %page
    #print(Hollys_url)
    # html = urllib.request.urlopen(blue_url)
    req = Request(blue_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage=urlopen(req).read()

    soupBlues = BeautifulSoup(webpage, 'html.parser')
    
    
    # tag_list = soupBlues.find('ul', class_="petition_list")
    tag_list = soupBlues.select_one('ul.petition_list')
    #  
    titles = tag_list.select_one('ul> li > div > div.bl_no')
    # for title in titles:
    print(titles.string)
    # 
    for article in tag_list.find_all('li'):
        #번호
        article_no = article.find_all('div',class_="bl_no")
        article_no.text
        print('ㅠㅠ')
        print("제목"+article_no)
        #제목
        article_name = article.find_all('div',class_="bl_subject").get_text()
        #청원 종료일
        article_date = article.find_all('div',class_="bl_date").get_text()
        #참여인원
        article_agree = article.find_all('div',class_="bl_agree").get_text()
        result.append([article_no]+[article_name]+[article_date]+[article_agree])
    
# hollys_tbl = pd.DataFrame(result, columns = ('store', 'sido-gu', 'address', 'phone'))
print(result)
#hollys_tbl.to_csv('./hollys.csv', encoding ='cp949', mode='w', index=True)
# del result[:]