from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Wired',
        'url': 'https://www.wired.com',
    }

    FEED_URL = 'https://www.wired.com/feed/rss'
