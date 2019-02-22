from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Guardian',
        'category': 'science',
        'url': 'https://www.theguardian.com',
    }

    FEED_URL = 'https://www.theguardian.com/science/rss'
