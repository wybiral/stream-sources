from sources.washingtonpost._source import WapoSource

class Source(WapoSource):

    SOURCE = {
        'name': 'Washington Post (Politics)',
        'url': 'https://www.washingtonpost.com',
    }

    FEED_URL = 'https://www.washingtonpost.com/politics/?resType=rss'
