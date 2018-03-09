from sources.generic import FeedSource
from . import business, gadgets, science, security, software

class Source(FeedSource):

    SOURCE = {
        'name': 'Ars Technica',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/index'
