from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Reuters (Top News)',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'http://feeds.reuters.com/reuters/topNews'
