from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Guardian',
        'category': 'world',
        'url': 'https://www.theguardian.com',
    }

    FEED_URL = 'https://www.theguardian.com/world/rss'
