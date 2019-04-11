from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Slate',
        'category': 'politics',
        'url': 'https://slate.com',
    }

    FEED_URL = 'https://slate.com/feeds/news-and-politics.rss'
