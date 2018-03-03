from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Gear & Gadgets)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/gadgets'

update = generic_feed.create_update(FEED_URL, SOURCE)
