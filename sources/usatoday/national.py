from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'USA Today (National)',
        'url': 'https://www.usatoday.com',
    }

    FEED_URL = 'http://rssfeeds.usatoday.com/usatodaycomnation-topstories&x=1'
