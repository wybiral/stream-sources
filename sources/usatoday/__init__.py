from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'USA Today',
        'url': 'https://www.usatoday.com',
    }

    FEED_URL = 'http://rssfeeds.usatoday.com/usatoday-newstopstories&x=1'
