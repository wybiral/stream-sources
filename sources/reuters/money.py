from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Money)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/news/wealth'

update = generic_feed.create_update(FEED_URL, SOURCE)
