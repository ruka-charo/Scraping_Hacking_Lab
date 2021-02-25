from selenium import webdriver
import time


url = 'https://srad.jp/'


#WebDriver
driver = webdriver.Safari()
driver.get(url)


#ウィンドウの大きさ調整
width = driver.execute_script('return document.body.scrollWidth')
height = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(width, height)


#スクリーンショットを撮る
time.sleep(3)
driver.save_screenshot('screenshot.png')


#ウィンドウを閉じる
time.sleep(5)
driver.quit()
