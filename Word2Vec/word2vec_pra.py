%cd /Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/9_Scraping_Hacking_Lab/MeCab
import MeCab
import requests
from bs4 import BeautifulSoup


domain = 'https://ja.wikipedia.org/wiki/'
names = ['森鴎外', '夏目漱石', '島崎藤村', '与謝野晶子', '坪内逍遥', '石川啄木',
    '谷崎潤一郎', '芥川龍之介', '川端康成', '志賀直哉', '中原中也', '太宰治', '大岡昇平',
    '三島由紀夫']

m = MeCab.Tagger('-Owakati')
corpus = []

for name in names:
    with requests.get(domain + name) as response:
        soup = BeautifulSoup(response.content, 'html.parser')
        p_text = soup.find_all('p')

        for p in p_text:
            corpus.append(m.parse(p.text).strip())

with open('data.txt', 'w') as file:
    file.write('\n'.join(corpus))
