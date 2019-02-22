from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Hill',
        'category': 'senate',
        'url': 'https://thehill.com',
    }

    FEED_URL = 'http://thehill.com/taxonomy/term/1130/feed'
