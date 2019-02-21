from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'USA Today (Washington)',
        'url': 'https://www.usatoday.com',
    }

    FEED_URL = 'http://rssfeeds.usatoday.com/usatodaycomwashington-topstories&x=1'
