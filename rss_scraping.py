import feedparser


rss_url = 'https://b.hatena.ne.jp/hotentry/knowledge.rss'

feed = feedparser.parse(rss_url)

for entry in feed.entries:
    print(entry.title)
    print(entry.link)
