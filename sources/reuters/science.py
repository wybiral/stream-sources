from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Science)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/reuters/scienceNews'

update = generic_feed.create_update(FEED_URL, SOURCE)
