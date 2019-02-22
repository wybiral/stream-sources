from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Hill',
        'category': 'administration',
        'url': 'https://thehill.com',
    }

    FEED_URL = 'https://thehill.com/taxonomy/term/1132/feed'
