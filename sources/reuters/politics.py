from sources.reuters._source import ReutersSource


class Source(ReutersSource):

    SOURCE = {
        'name': 'Reuters (Politics)',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'http://feeds.reuters.com/Reuters/PoliticsNews'
