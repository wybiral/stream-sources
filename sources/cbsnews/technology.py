from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'CBS News',
        'category': 'technology',
        'url': 'https://www.cbsnews.com',
    }

    FEED_URL = 'https://www.cbsnews.com/latest/rss/tech'

    def filter(self, entry):
        if '/live/' in entry['link']:
            return False
        return True