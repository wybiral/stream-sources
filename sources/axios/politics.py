from sources.axios._source import AxiosSource


class Source(AxiosSource):

    SOURCE = {
        'name': 'Axios',
        'category': 'politics',
        'url': 'https://www.axios.com/',
    }

    FEED_URL = 'https://api.axios.com/feed/politics/'
