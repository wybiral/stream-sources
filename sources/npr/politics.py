from sources.npr._source import NprSource


class Source(NprSource):

    SOURCE = {
        'name': 'NPR News',
        'category': 'politics',
        'url': 'https://www.npr.org/sections/news/',
    }

    FEED_URL = 'https://www.npr.org/feeds/1014/feed.json'
