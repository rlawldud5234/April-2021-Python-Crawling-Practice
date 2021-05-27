from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd

#결과 배열
result=[]
#page수
pagelength = 0

print("==영화 평점 년도별 조회==")
year = input('검색하려는 년도를 적어주세요 ex/2020 : ')
url = 'https://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected=%s&sort=desc&view=detailed' % year
#url open
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage=urlopen(req).read()
soupmovie = BeautifulSoup(webpage, 'html.parser')
# page수 계산
pageul = soupmovie.find('ul', class_="pages")
for i in pageul.find_all('li'):
    pagelength += 1

# page에 따른 리퀘스트 반복
for page in range(pagelength):
    urlpage = 'https://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected=%s&sort=desc&view=detailed&page=%s' % (year,page)
    reqpage = Request(urlpage, headers={'User-Agent' : 'Mozilla/5.0'})
    html=urlopen(reqpage).read()
    soupHollys = BeautifulSoup(html, 'html.parser')
    #테이블 find_all로 찾기
    tag_tbody = soupHollys.find_all('table',class_="clamp-list")
    
    #tr마다 값들 찾아 result배열에 넣기
    for tbody in tag_tbody:
        for movie in tbody.find_all('tr'):
            if(str(movie)=='<tr class="spacer"></tr>'):
                continue
            #순번
            index = movie.find('span',class_="numbered")
            index = index.get_text()
            index = index.replace(' ', '')
            index = index.replace('\n','')
            print("num : " + index)
            #제목
            title_a = movie.find('a',class_="title")
            title= title_a.find('h3').get_text()
            print("title: " + title)
            #출시일
            date_div = movie.find('div', class_="clamp-details")
            date = date_div.find('span').get_text()
            print("date: " + date)
            #소개
            summary = movie.find('div', class_="summary").get_text()
            print("summary: " + summary)
            #평점
            score = movie.find('div', class_="metascore_w").get_text()
            print("score : " + score)
            print("=======================")
            
            result.append([index]+[title]+[date]+[summary]+[score])
#저장
movie_tbl = pd.DataFrame(result, columns = ('index', 'title', 'date', 'summary','score'))
movie_tbl.to_csv('./movie2.csv', encoding ='cp949', mode='w', index=True)
del result[:]