from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Atlantic',
        'category': 'us',
        'url': 'https://www.theatlantic.com',
    }

    FEED_URL = 'https://www.theatlantic.com/feed/channel/national/'
