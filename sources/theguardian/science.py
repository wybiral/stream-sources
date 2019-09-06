from sources.theguardian._source import TheGuardianSource


class Source(TheGuardianSource):

    SOURCE = {
        'name': 'The Guardian',
        'category': 'science',
        'url': 'https://www.theguardian.com',
    }

    FEED_URL = 'https://www.theguardian.com/science/rss'
