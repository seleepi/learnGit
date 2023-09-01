import requests
from bs4 import BeautifulSoup



def blogTop10(search):
    print('search for ' + search + '...')
    data = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=45&where=view&api_type=11&start=1&query={search}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=91&sm=tab_jum&ssc=tab.view.view&ngn_country=DE&lgl_rcode=&fgn_region=Lower%20Saxony&fgn_city=G%C3%B6ttingen&lgl_lat=&lgl_long=&abt=&_callback=viewMoreContents')
    soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')
    list = soup.select('a.api_txt_lines')
    return list


list = blogTop10('사과')

for i in range(10):
    print(str(i+1) + '. ' + list[i].text + '\n\t' + list[i]['href'])


