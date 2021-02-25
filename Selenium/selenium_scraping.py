#Google検索結果はスクレイピングできない。

from selenium import webdriver
from bs4 import BeautifulSoup
import time


#検索用語
url = 'https://www.google.com'
keyword = 'スクレイピング'

#WebDriver
driver = webdriver.Safari()
driver.get(url)
time.sleep(3)

#遠隔で入力、検索
search = driver.find_element_by_name('q')
search.send_keys(keyword)
search.submit()

#スクレイピング
soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find_all('h3', attrs={'class': 'LC201b'})

for result in results:
    print(result.get_text())

#ブラウザを閉じる
time.sleep(5)
driver.quit()
