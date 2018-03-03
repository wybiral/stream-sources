from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Cars Technica)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/cars'

update = generic_feed.create_update(FEED_URL, SOURCE)

