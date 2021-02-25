from selenium import webdriver
import time


#遠隔で検索
url = 'https://www.google.com'
keyword = 'スクレイピング'

#WebDriver
driver = webdriver.Safari()
driver.get(url)
time.sleep(3)

#遠隔で入力
search = driver.find_element_by_name('q')
search.send_keys(keyword)
search.submit()

#ブラウザを閉じる
time.sleep(5)
driver.quit()
