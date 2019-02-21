from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Hill (Administration)',
        'url': 'https://thehill.com',
    }

    FEED_URL = 'https://thehill.com/taxonomy/term/1132/feed'
