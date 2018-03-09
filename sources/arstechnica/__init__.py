from sources.generic import FeedSource


class ArsTechnica(FeedSource):

    SOURCE = {
        'name': 'Ars Technica',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/index'
