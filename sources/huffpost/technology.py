from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'HuffPost',
        'category': 'technology',
        'url': 'https://www.huffpost.com',
    }

    FEED_URL = 'https://www.huffpost.com/section/technology/feed'
