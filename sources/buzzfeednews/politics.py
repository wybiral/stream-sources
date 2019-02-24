from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'BuzzFeed News',
        'category': 'politics',
        'url': 'https://www.buzzfeednews.com',
    }

    FEED_URL = 'https://www.buzzfeednews.com/section/politics.xml'
