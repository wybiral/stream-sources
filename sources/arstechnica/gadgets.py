from sources.generic import FeedSource


class ArsTechnicaGadgets(FeedSource):

    SOURCE = {
        'name': 'Ars Technica (Gear & Gadgets)',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/gadgets'
