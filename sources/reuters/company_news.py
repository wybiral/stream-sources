from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Company News)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/reuters/companyNews'

update = generic_feed.create_update(FEED_URL, SOURCE)
