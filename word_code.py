import requests


#%%url先のサイトが何の文字コードで書かれているか
url = 'https://kakaku.com/'
response = requests.get(url)
encoding = response.apparent_encoding
print(encoding)

#%%文字化けを修正
url = 'https://kakaku.com/'
response = requests.get(url)
response.encoding = response.apparent_encoding
print(response.text)
