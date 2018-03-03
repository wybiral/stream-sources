from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Pictures)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/ReutersPictures'

update = generic_feed.create_update(FEED_URL, SOURCE)
