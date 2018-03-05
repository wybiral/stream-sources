from sources import generic_feed

SOURCE = {
    'name': 'Threatpost',
    'url': 'https://threatpost.com/',
}

FEED_URL = 'https://threatpost.com/feed/'

update = generic_feed.create_update(FEED_URL, SOURCE)
