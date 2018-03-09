from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Reuters (World)',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'http://feeds.reuters.com/Reuters/worldNews'
