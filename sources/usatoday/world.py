from sources.usatoday._source import UsaTodaySource


class Source(UsaTodaySource):

    SOURCE = {
        'name': 'USA Today (World)',
        'url': 'https://www.usatoday.com',
    }

    FEED_URL = 'http://rssfeeds.usatoday.com/usatodaycomworld-topstories&x=1'
