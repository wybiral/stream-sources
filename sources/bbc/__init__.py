from sources.generic import FeedSource
from . import business, science, technology, world


class Source(FeedSource):

    SOURCE = {
        'name': 'BBC News',
        'url': 'http://www.bbc.com/news',
    }

    FEED_URL = 'http://feeds.bbci.co.uk/news/rss.xml'
