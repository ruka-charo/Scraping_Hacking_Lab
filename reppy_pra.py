from reppy.robots import Robots

#%%
robots = Robots.fetch('https://allabout.co.jp/robots.txt')
agent = robots.agent('*')

#アクセス可能かどうか
agent.allowed('https://allabout.co.jp/r_finance/')
#agent.allowed('https://allabout.co.jp/ranking/daily/')


#%%クロール間隔の取得
robots = Robots.fetch('https://allabout.co.jp/robots.txt')
agent = robots.agent('bingbot')
agent.delay
