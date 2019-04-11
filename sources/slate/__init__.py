from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Slate',
        'url': 'https://slate.com',
    }

    FEED_URL = 'https://slate.com/feeds/all.rss'
