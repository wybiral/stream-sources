from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The New York Times',
        'url': 'https://www.nytimes.com',
    }

    FEED_URL = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
