from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'HuffPost',
        'category': 'world',
        'url': 'https://www.huffpost.com',
    }

    FEED_URL = 'https://www.huffpost.com/section/world-news/feed'
