from sources.theguardian._source import TheGuardianSource


class Source(TheGuardianSource):

    SOURCE = {
        'name': 'The Guardian',
        'category': 'technology',
        'url': 'https://www.theguardian.com',
    }

    FEED_URL = 'https://www.theguardian.com/us/technology/rss'
