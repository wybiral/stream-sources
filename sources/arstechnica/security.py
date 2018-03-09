from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Ars Technica (Risk Assessment)',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/security'
