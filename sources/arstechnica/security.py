from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Risk Assessment)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/security'

update = generic_feed.create_update(FEED_URL, SOURCE)
