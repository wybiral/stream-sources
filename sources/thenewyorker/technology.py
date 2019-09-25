from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The New Yorker',
        'category': 'technology',
        'url': 'https://www.newyorker.com',
    }

    FEED_URL = 'http://www.newyorker.com/feed/tech'
