from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'ABC News',
        'url': 'https://abcnews.go.com/',
    }

    FEED_URL = 'https://abcnews.go.com/abcnews/topstories'
