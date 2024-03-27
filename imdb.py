import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('ul.ipc-metadata-list > li')


for movie in movies:
    title = movie.select_one('h3.ipc-title__text').text
    year = movie.select_one('.cli-title-metadata > span').text
    rating = movie.select_one('.cli-ratings-container > span').text