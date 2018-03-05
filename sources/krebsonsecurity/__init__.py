from sources import generic_feed

SOURCE = {
    'name': 'Krebs on Security',
    'url': 'https://krebsonsecurity.com/',
}

FEED_URL = 'https://krebsonsecurity.com/feed/'

update = generic_feed.create_update(FEED_URL, SOURCE)
