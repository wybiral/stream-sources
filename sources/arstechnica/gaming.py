from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Opposable Thumbs)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/gaming'

update = generic_feed.create_update(FEED_URL, SOURCE)
