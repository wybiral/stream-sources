from bs4 import BeautifulSoup
import feedparser
import time

from sources import Source


class WapoSource(Source):

    def update(self):
        feed = feedparser.parse(self.FEED_URL)
        entries = feed['entries']
        for entry in reversed(entries):
            url = entry['link']
            if url in self.stream:
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
            update['source'] = self.SOURCE
            self.stream.push(update)
