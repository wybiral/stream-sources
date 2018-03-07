from sources import generic_feed

SOURCE = {
    'name': 'BleepingComputer',
    'url': 'https://www.bleepingcomputer.com/',
}

FEED_URL = 'https://www.bleepingcomputer.com/feed/'

update = generic_feed.create_update(FEED_URL, SOURCE)
