from sources.theguardian._source import TheGuardianSource


class Source(TheGuardianSource):

    SOURCE = {
        'name': 'The Guardian',
        'category': 'world',
        'url': 'https://www.theguardian.com',
    }

    FEED_URL = 'https://www.theguardian.com/world/rss'
