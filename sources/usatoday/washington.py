from sources.usatoday._source import UsaTodaySource


class Source(UsaTodaySource):

    SOURCE = {
        'name': 'USA Today (Washington)',
        'url': 'https://www.usatoday.com',
    }

    FEED_URL = 'http://rssfeeds.usatoday.com/usatodaycomwashington-topstories&x=1'
