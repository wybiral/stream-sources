from sources.npr._source import NprSource


class Source(NprSource):

    SOURCE = {
        'name': 'NPR News (World)',
        'url': 'https://www.npr.org/sections/news/',
    }

    FEED_URL = 'https://www.npr.org/feeds/1004/feed.json'
