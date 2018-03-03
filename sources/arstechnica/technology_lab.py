from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Technology Lab)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/technology-lab'

update = generic_feed.create_update(FEED_URL, SOURCE)

