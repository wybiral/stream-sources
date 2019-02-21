from sources.usatoday._source import UsaTodaySource


class Source(UsaTodaySource):

    SOURCE = {
        'name': 'USA Today (National)',
        'url': 'https://www.usatoday.com',
    }

    FEED_URL = 'http://rssfeeds.usatoday.com/usatodaycomnation-topstories&x=1'
