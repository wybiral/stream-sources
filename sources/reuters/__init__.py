from sources.reuters._source import ReutersSource
from . import business, money, politics, science, technology, us, world


class Source(ReutersSource):

    SOURCE = {
        'name': 'Reuters (Top News)',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'http://feeds.reuters.com/reuters/topNews'
