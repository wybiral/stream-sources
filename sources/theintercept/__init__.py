from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Intercept',
        'url': 'https://theintercept.com/',
    }

    FEED_URL = 'https://theintercept.com/feed/?lang=en'
