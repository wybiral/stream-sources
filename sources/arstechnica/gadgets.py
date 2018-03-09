from sources.arstechnica._source import ArsSource


class Source(ArsSource):

    SOURCE = {
        'name': 'Ars Technica (Gear & Gadgets)',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/gadgets'
