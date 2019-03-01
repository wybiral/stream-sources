from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'BBC News',
        'url': 'http://www.bbc.com/news',
    }

    FEED_URL = 'http://feeds.bbci.co.uk/news/rss.xml'

    def filter(self, entry):
        if '/sport/' in entry['link']:
            return False
        return True