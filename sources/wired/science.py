from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Wired (Science)',
        'url': 'https://www.wired.com',
    }

    FEED_URL = 'https://www.wired.com/feed/category/science/latest/rss'
