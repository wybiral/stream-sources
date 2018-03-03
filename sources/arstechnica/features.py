from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Features)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/features'

update = generic_feed.create_update(FEED_URL, SOURCE)

