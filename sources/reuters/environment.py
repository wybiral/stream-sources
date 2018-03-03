from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Environment)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/reuters/environment'

update = generic_feed.create_update(FEED_URL, SOURCE)
