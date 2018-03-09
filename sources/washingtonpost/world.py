from sources.washingtonpost._source import WapoSource

class Source(WapoSource):

    SOURCE = {
        'name': 'Washington Post (World)',
        'url': 'https://www.washingtonpost.com',
    }

    FEED_URL = 'https://www.washingtonpost.com/world/?resType=rss'
