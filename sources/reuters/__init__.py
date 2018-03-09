from sources.generic import FeedSource
from . import business, money, politics, science, technology, us, world


class Source(FeedSource):

    SOURCE = {
        'name': 'Reuters (Top News)',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'http://feeds.reuters.com/reuters/topNews'
