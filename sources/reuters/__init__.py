from sources.reuters._source import ReutersSource


class Source(ReutersSource):

    SOURCE = {
        'name': 'Reuters (Top News)',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'http://feeds.reuters.com/reuters/topNews'
