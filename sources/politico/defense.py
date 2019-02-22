from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Politico',
        'category': 'defense',
        'url': 'https://www.politico.com',
    }

    FEED_URL = 'https://www.politico.com/rss/defense.xml'
