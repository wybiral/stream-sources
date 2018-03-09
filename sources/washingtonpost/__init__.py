from sources.washingtonpost._source import WapoSource
from . import business, national, politics, technology, world

class Source(WapoSource):

    SOURCE = {
        'name': 'Washington Post',
        'url': 'https://www.washingtonpost.com',
    }

    FEED_URL = 'https://www.washingtonpost.com/?resType=rss'
