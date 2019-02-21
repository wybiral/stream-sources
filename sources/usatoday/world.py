from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'USA Today (World)',
        'url': 'https://www.usatoday.com',
    }

    FEED_URL = 'http://rssfeeds.usatoday.com/usatodaycomworld-topstories&x=1'
