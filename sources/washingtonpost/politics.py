from sources.washingtonpost import parser

SOURCE = {
    'name': 'Washington Post (Politics)',
    'url': 'https://www.washingtonpost.com',
}

FEED_URL = 'https://www.washingtonpost.com/politics/?resType=rss'

update = parser.create_update(FEED_URL, SOURCE)
