from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Ars Technica (Ministry of Innovation)',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/business'
