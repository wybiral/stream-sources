from sources.reuters._source import ReutersSource


class Source(ReutersSource):

    SOURCE = {
        'name': 'Reuters (Money)',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'http://feeds.reuters.com/news/wealth'
