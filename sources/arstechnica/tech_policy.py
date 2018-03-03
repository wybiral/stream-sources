from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Law & Disorder)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/tech-policy'

update = generic_feed.create_update(FEED_URL, SOURCE)
