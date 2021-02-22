import requests


proxy = {
'http':'http://プロキシサーバーのIPアドレス:ポート番号',
'https':'http://プロキシサーバーのIPアドレス:ポート番号'
}

response = requests.get('https://www.google.com', proxies=proxy).content
