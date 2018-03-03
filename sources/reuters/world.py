from sources import generic_feed

SOURCE = {
    'name': 'Reuters (World)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/Reuters/worldNews'

update = generic_feed.create_update(FEED_URL, SOURCE)
