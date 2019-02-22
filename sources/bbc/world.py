from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'BBC News',
        'category': 'world',
        'url': 'http://www.bbc.com/news',
    }

    FEED_URL = 'http://feeds.bbci.co.uk/news/world/rss.xml'
