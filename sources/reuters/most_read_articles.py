from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Most Read Articles)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/reuters/MostRead'

update = generic_feed.create_update(FEED_URL, SOURCE)
