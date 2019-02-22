from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'HuffPost',
        'category': 'politics',
        'url': 'https://www.huffpost.com',
    }

    FEED_URL = 'https://www.huffpost.com/section/politics/feed'
