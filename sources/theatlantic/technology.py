from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Atlantic',
        'category': 'technology',
        'url': 'https://www.theatlantic.com',
    }

    FEED_URL = 'https://www.theatlantic.com/feed/channel/technology/'
