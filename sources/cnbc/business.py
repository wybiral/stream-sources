from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'CNBC',
        'category': 'business',
        'url': 'https://www.cnbc.com',
    }

    FEED_URL = 'https://www.cnbc.com/id/10001147/device/rss/rss.html'
