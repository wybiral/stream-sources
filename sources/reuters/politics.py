from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Politics)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/Reuters/PoliticsNews'

update = generic_feed.create_update(FEED_URL, SOURCE)
