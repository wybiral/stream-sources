from sources import generic_feed

SOURCE = {
    'name': 'Reuters (Arts)',
    'url': 'https://www.reuters.com',
}

FEED_URL = 'http://feeds.reuters.com/news/artsculture'

update = generic_feed.create_update(FEED_URL, SOURCE)
