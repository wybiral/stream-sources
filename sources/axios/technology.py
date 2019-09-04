from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Axios',
        'category': 'technology',
        'url': 'https://www.axios.com/',
    }

    FEED_URL = 'https://api.axios.com/feed/technology/'
