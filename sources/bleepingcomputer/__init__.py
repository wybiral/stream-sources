from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'BleepingComputer',
        'url': 'https://www.bleepingcomputer.com/',
    }

    FEED_URL = 'https://www.bleepingcomputer.com/feed/'
