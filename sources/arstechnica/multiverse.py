from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (The Multiverse)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/multiverse'

update = generic_feed.create_update(FEED_URL, SOURCE)
