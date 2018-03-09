from sources.generic import FeedSource


class ArsTechnicaScience(FeedSource):

    SOURCE = {
        'name': 'Ars Technica (The Scientific Method)',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/science'
