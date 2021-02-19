import requests


url = 'http://httpbin.org/user-agent'

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6)\
AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"

headers = {
    'User-Agent': user_agent
}


requests.get(url, headers=headers).text
