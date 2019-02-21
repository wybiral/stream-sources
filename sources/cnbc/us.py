from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'CNBC (US)',
        'url': 'https://www.cnbc.com',
    }

    FEED_URL = 'https://www.cnbc.com/id/15837362/device/rss/rss.html'
