import requests
from bs4 import BeautifulSoup


url = requests.get('https://allabout.co.jp/')
soup = BeautifulSoup(url.content, 'html.parser')
nofolow = soup.find('meta', attrs={'content': 'nofollow'})

print(nofolow)
