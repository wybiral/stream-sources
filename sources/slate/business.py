from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Slate',
        'category': 'business',
        'url': 'https://slate.com',
    }

    FEED_URL = 'https://slate.com/feeds/business.rss'
