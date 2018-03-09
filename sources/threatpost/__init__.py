from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Threatpost',
        'url': 'https://threatpost.com/',
    }

    FEED_URL = 'https://threatpost.com/feed/'
