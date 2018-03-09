from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Ars Technica (Software)',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/software'
