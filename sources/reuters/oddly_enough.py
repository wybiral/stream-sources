from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Oddly Enough)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/reuters/oddlyEnoughNews'

update = generic_feed.create_update(FEED_URL, SOURCE)
