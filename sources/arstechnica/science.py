from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (The Scientific Method)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/science'

update = generic_feed.create_update(FEED_URL, SOURCE)
