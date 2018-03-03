from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Ministry of Innovation)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/business'

update = generic_feed.create_update(FEED_URL, SOURCE)
