from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Top News)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/reuters/topNews'

update = generic_feed.create_update(FEED_URL, SOURCE)
