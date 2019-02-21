from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The Hill',
        'url': 'https://thehill.com',
    }

    FEED_URL = 'https://thehill.com/rss/syndicator/19109'
