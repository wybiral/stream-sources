from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Hill (House)',
        'url': 'https://thehill.com',
    }

    FEED_URL = 'http://thehill.com/taxonomy/term/1131/feed'
