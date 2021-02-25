#Google検索結果はスクレイピングできない。

#最新のWebdriverをインストールしてから実行。
'''
 from selenium import webdriver
 from webdriver_manager.chrome import ChromeDriverManager

 driver = webdriver.Chrome(ChromeDriverManager().install())
 driver.get(url)
'''


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


url = "https://www.google.com"
keyword = 'スクレイピング'


#ヘッドレスの設定
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

#webdriver
driver.get(url)
time.sleep(3)

#自動入力
search = driver.find_element_by_name('q')
search.send_keys(keyword)
search.submit()

#スクレイピング
soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find_all('h3', attrs={'class': 'LC201b'})

#データの取り出し
for result in results:
    print(result.get_text())

#ウインドウを閉じる
time.sleep(5)
driver.quit()
