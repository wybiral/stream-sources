from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Guardian',
        'category': 'business',
        'url': 'https://www.theguardian.com',
    }

    FEED_URL = 'https://www.theguardian.com/us/business/rss'
