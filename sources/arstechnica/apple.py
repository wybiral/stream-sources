from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Infinite Loop)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/apple'

update = generic_feed.create_update(FEED_URL, SOURCE)
