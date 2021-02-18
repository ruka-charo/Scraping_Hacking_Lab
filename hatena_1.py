import requests
from bs4 import BeautifulSoup


#準備
url = 'https://b.hatena.ne.jp'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


#情報の取り出し
top_entry = soup.find('section', attrs={'class': 'entrylist-unit'})
entries = top_entry.find_all('div', attrs={'class': 'entrylist-contents-main'})

for entry in entries:
    title_tag = entry.find('h3', attrs={'class': 'entrylist-contents-title'})
    title = title_tag.find('a').get('title')

    users_tag = entry.find('span', attrs={'class': 'entrylist-contents-users'})
    users = users_tag.get_text().strip()

    print(title)
    print(users)
