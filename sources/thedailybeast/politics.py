from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Daily Beast',
        'category': 'politics',
        'url': 'https://www.thedailybeast.com/',
    }

    FEED_URL = 'https://feeds.thedailybeast.com/rss/politics'
