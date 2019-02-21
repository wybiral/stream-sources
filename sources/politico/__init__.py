from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Politico',
        'url': 'https://www.politico.com',
    }

    FEED_URL = 'https://www.politico.com/rss/politics08.xml'
