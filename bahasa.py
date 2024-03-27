import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

url = 'https://statisticstimes.com/tech/top-computer-languages.php'

data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

bahasa = soup.select('#table_id > tbody >tr')

for bhs in bahasa:
    nama = bhs.select_one('.name').text
    rating = bhs.select_one('td:nth-child(5)').text
    print(rating)
