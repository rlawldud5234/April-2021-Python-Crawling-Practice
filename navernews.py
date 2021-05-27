from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import pandas as pd

result=[]

for page in range(1, 10):
    news_url = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105#&date=%d2000:00:00&page=1' %page
    #print(Hollys_url)
    # html = urllib.request.urlopen(blue_url)
    req = Request(news_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage=urlopen(req).read()

    soupNews = BeautifulSoup(webpage, 'html.parser')
    
    # tag_list = soupBlues.find('ul', class_="petition_list")
    tag_list = soupNews.select_one('ul.cluster_list')
    #  
    titles = tag_list.select_one('ul> li > div.cluster_text')
    # for title in titles:
    print(titles.string)
    # 
    for article in tag_list.find('li'):

        #번호
        article_no = article.find_all('div',class_="cluster_text")
        article_no.text
        # print('ㅠㅠ')
        # print("제목"+article_no)
        #내용
        article_name = article.find_all('div',class_="cluster_text_lede").get_text()

        article_name = soupNew.find
        #회사명
        article_date = article.find_all('div',class_="cluster_text_info").get_text()
        #참여인원
        # article_agree = article.find_all('div',class_="bl_agree").get_text()
        result.append([article_no]+[article_name]+[article_date])
    
# hollys_tbl = pd.DataFrame(result, columns = ('store', 'sido-gu', 'address', 'phone'))
print(result)
#hollys_tbl.to_csv('./hollys.csv', encoding ='cp949', mode='w', index=True)
# del result[:]