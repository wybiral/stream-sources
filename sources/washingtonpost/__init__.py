from sources.washingtonpost import parser

SOURCE = {
    'name': 'Washington Post',
    'url': 'https://www.washingtonpost.com',
}

FEED_URL = 'https://www.washingtonpost.com/?resType=rss'

update = parser.create_update(FEED_URL, SOURCE)
