import requests
from sources import Source


class NprSource(Source):

    def update(self):
        r = requests.get(self.FEED_URL)
        data = r.json()
        for item in data['items']:
            url = item['url']
            url, _ = url.split('?', 1)
            if url in self.stream:
                continue
            update = {}
            update['url'] = url
            date = item['date_published']
            date = date[:19].replace('T', ' ')
            update['date'] = date
            update['title'] = item['title']
            if 'summary' in item:
                update['body'] = item['summary']
            if 'image' in item:
                update['thumb'] = item['image']
            update['source'] = self.SOURCE
            self.stream.push(update)
