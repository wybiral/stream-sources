from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The New York Times',
        'category': 'us',
        'url': 'https://www.nytimes.com',
    }

    FEED_URL = 'http://rss.nytimes.com/services/xml/rss/nyt/US.xml'
