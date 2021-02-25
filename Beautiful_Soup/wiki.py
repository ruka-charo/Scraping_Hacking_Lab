import requests
from bs4 import BeautifulSoup
import csv
import re


#準備
url = 'https://ja.wikipedia.org/'
response = requests.get(url)

#第一取り出し
soup = BeautifulSoup(response.content, 'html.parser')
today = soup.find('div', attrs={'id': 'on_this_day'})

#取り出した情報をリスト化
today_list = []
entries = today.find_all('li')

for i, entry in enumerate(entries):
    #全角カッコを半角に変換して検索しやすくする
    today_text = entry.get_text().replace('（', '(').replace('）', ')')
    match = re.search('\((\d*?)年\)', today_text)
    if match:
        today_list.append([i+1, entry.get_text(), match.group(1)])
    else:
        today_list.append([i+1, entry.get_text()])


#csvに保存
with open('output.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(today_list)
