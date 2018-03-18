from sources.npr._source import NprSource
from . import business, politics, science, technology, world

class Source(NprSource):

    SOURCE = {
        'name': 'NPR News',
        'url': 'https://www.npr.org/sections/news/',
    }

    FEED_URL = 'https://www.npr.org/feeds/1001/feed.json'
