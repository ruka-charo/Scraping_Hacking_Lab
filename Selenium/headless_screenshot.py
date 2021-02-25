from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


url = 'https://hatenablog.com/'

#ヘッドレス設定
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

#ウインドウサイズの調整
driver.get(url)
width = driver.execute_script('return document.body.scrollWidth')
height = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(width, height)

#スクリーンショット
time.sleep(3)
driver.save_screenshot('screenshot.png')

#ウインドウを閉じる
time.sleep(3)
driver.quit()
