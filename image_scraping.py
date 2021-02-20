import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import uuid


#フォルダの作成
output_folder = Path('nobunaga')
output_folder.mkdir(exist_ok=True)

#スクレイピング準備
url = 'https://ja.wikipedia.org/wiki/織田信長'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#画像の抽出
content = soup.find('div', attrs={'id': 'bodyContent'})
images = content.find_all('img')

for image in images:
    long_image_url = urllib.parse.urljoin(url, image['src'])
    image_data = requests.get(long_image_url)
    with open(str('./nobunaga/') + str(uuid.uuid4()) + str('.jpeg'), 'wb') as f:
        f.write(image_data.content)
