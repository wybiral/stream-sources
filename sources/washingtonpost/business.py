from sources.washingtonpost import parser

SOURCE = {
    'name': 'Washington Post (Business)',
    'url': 'https://www.washingtonpost.com',
}

FEED_URL = 'https://www.washingtonpost.com/business/?resType=rss'

update = parser.create_update(FEED_URL, SOURCE)
