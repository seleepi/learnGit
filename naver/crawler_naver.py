# 크롤러의 기본
# 브라우저가 아닌 파이썬으로 데이터 들어있는 웹사이트 접속(그럼 HTML 도착)
# HTML 분석 툴에 집어넣어서 필요한 정보를 추출
# pip request : request 라이브러리를 설치

import requests # 파이썬으로 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 파이선으로 HTML 웹문서 분석 도와주는 라이브러리
import urllib.request

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

#print(data)
#print(data.content)
print(data.status_code) #200: funktioniert gut, 400 or 500: falsch

soup = BeautifulSoup(data.content, 'html.parser') #data von HTML wird schöner
#print(soup)
print(soup.find_all('strong', id="_nowVal")) #find all of Tag:strong with attribute id:nowVal
#result: list
#print(soup.find_all('strong', id="_nowVal")[0]) << indexing, then element of list
print(soup.find_all('strong', id="_nowVal")[0].text) #data only, no html
print(soup.find_all('span', class_="tah")) #class is reserved word in python
#when space in class name, it's multiple class name(ex. class = tah p11). use only one for search


#CSS selector
#class, id 하나도 없는 요소: select()와 상위에 있는 요소들을 이용
soup.select('.gray .f_down em')[0].text #'.': class in css, '#': id in css, without any of them: tag
#내부 요소를 찾으려면 띄어쓰기. search em tag in f_down class in gray class
soup.select('strong#_nowVal') #and를 쓰려면 띄어쓰기 없이 쓰면 됨 # 'tag.class#id'

#image
image = soup.select('#img_chart_area')[0]
urllib.request.urlretrieve(image['src'], 'image.jpg') #save (imageUrl, 'path')
#print(image['src'])