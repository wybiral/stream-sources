from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Krebs on Security',
        'url': 'https://krebsonsecurity.com/',
    }

    FEED_URL = 'https://krebsonsecurity.com/feed/'
