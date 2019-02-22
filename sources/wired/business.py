from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Wired',
        'category': 'business',
        'url': 'https://www.wired.com',
    }

    FEED_URL = 'https://www.wired.com/feed/category/business/latest/rss'
