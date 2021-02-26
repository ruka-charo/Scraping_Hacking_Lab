import MeCab
import requests
from bs4 import BeautifulSoup

#%%
m = MeCab.Tagger()
print(m.parse('すもももももももものうち'))

#%%
url = 'https://ja.wikipedia.org/wiki/Google_Pixel'
m = MeCab.Tagger()

#スクレイピング
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.find('p').get_text()

#形態素解析
parse_text = m.parse(text)
print(parse_text)


#分かち書き%%
url = 'https://ja.wikipedia.org/wiki/Google_Pixel'
m = MeCab.Tagger('-Owakati')

#スクレイピング
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.find('p').get_text()

#形態素解析
parse_text = m.parse(text)
print(parse_text)
