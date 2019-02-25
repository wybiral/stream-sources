from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'VICE',
        'category': 'technology',
        'url': 'https://www.vice.com',
    }

    FEED_URL = 'https://www.vice.com/en_us/rss/topic/technology'
