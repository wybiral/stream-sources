from sources.washingtonpost._source import WapoSource

class Source(WapoSource):

    SOURCE = {
        'name': 'Washington Post (Technology)',
        'url': 'https://www.washingtonpost.com',
    }

    FEED_URL = 'https://www.washingtonpost.com/business/technology/?resType=rss'
