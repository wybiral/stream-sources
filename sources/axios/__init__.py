from sources.axios._source import AxiosSource


class Source(AxiosSource):

    SOURCE = {
        'name': 'Axios',
        'url': 'https://www.axios.com/',
    }

    FEED_URL = 'https://api.axios.com/feed/'
