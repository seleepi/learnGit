import requests
from bs4 import BeautifulSoup
import urllib.request

#list = []
company = ['005930', '066575', '005380', '035720', '034220', '003490']

def current_val(code):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={code}') # f'문자{변수}문자'
    soup = BeautifulSoup(data.content, 'html.parser') # in html we don't use \, but used for ex. url. remove it
    #print(soup.find_all('span', class_="tah")[5].text)
    #list.append(soup.find_all('strong', id="_nowVal")[0].text)
    return soup.find_all('strong', id="_nowVal")[0].text

file = open('currentVal.txt', 'w')
for i in company:
    file.write(current_val(i) + '\n')
file.close()

file = open('currentVal.txt', 'r')
print(file.read())
file.close()



# url을 받아올 때 백슬래쉬가 포함돼있을 수 있는데 html에서는 백슬래쉬를 안다루므로
# data.text.replace('\\', '')으로 제거하자
# data.content는 object라서 txt로 가져와야 replace 사용 가능


# 네이버 블로그 따오기
#무한 스크롤 따오는 방법은 이하 생략
soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')
articleList = soup.select('a.api_txt_lines') # tag a class api_txt_lines
print(articleList[0]) # all html of 'a' Tag
print(articleList[0].text) # print olny inhalt(als txt)
print(articleList[0]['href']) # 주소를 담은 속성

# query=사과 <- 검색어
# &는 구분기호