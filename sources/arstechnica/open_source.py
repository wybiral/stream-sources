from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Open Source)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/open-source'

update = generic_feed.create_update(FEED_URL, SOURCE)
