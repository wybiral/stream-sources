from sources import generic_feed

SOURCE = {
    'name': 'Ars Technica (Staff Blogs)',
    'url': 'https://arstechnica.com',
}

FEED_URL = 'http://feeds.arstechnica.com/arstechnica/staff-blogs'

update = generic_feed.create_update(FEED_URL, SOURCE)

