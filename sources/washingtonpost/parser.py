from bs4 import BeautifulSoup
import feedparser
import time

def create_update(feed_url, source):
    def update(stream):
        feed = feedparser.parse(feed_url)
        entries = feed['entries']
        for entry in reversed(entries):
            url = entry['link']
            if url in stream:
                continue
            update = {}
            update['url'] = url
            update['title'] = entry['title']
            if 'summary' in entry:
                update['body'] = entry['summary']
            if 'media_content' in entry:
                update['thumb'] = entry['media_content'][0]['url']
            try:
                _, rest = url.split('/wp/', 1)
                parts = rest.split('/')
                date = '-'.join(parts[:3])
            except ValueError:
                parts = url.split('/')
                date = '-'.join(parts[-4:-1])
            update['date'] = date
            update['source'] = source
            stream.push(update)
    return update
