from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'CNBC',
        'url': 'https://www.cnbc.com',
    }

    FEED_URL = 'https://www.cnbc.com/id/100003114/device/rss/rss.html'
