import requests
from bs4 import BeautifulSoup
import urllib


#相対URLを絶対URLに変換
url = 'https://kakaku.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

category_url = soup.find('a', attrs={'class': 'p-catList_cell'}).get('href')
long_category_url = urllib.parse.urljoin(url, category_url)

print(long_category_url)
