from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/index'

update = generic_feed.create_update(FEED_URL, SOURCE)
