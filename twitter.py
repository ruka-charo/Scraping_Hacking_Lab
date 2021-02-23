from selenium import webdriver
import time


username = 'ruka_charo1'
password = '96520411Sa'
text = 'seleniumを用いて自動Tweetの練習中。ツイートされていたらミスったと思ってください。'

url = 'https://twitter.com/login'


#WebDriver
driver = webdriver.Safari()
driver.get(url)
time.sleep(3)


#ログイン
username_form = driver.find_element_by_name('session[username_or_email]')
password_form = driver.find_element_by_name('session[password]')
username_form.send_keys(username)
password_form.send_keys(password)
password_form.submit()


#ツイート内容を記入
time.sleep(3)
tweet_area = driver.find_element_by_class_name('notranslate')
tweet_area.send_keys(text)


#ブラウザを閉じる
time.sleep(5)
driver.quit()
