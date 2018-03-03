from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Ars Cardboard)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/cardboard'

update = generic_feed.create_update(FEED_URL, SOURCE)

