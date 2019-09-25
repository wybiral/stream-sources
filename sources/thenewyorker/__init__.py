from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The New Yorker',
        'url': 'https://www.newyorker.com',
    }

    FEED_URL = 'http://www.newyorker.com/feed/news'
