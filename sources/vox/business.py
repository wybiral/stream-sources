from sources.vox._source import VoxSource


class Source(VoxSource):

    SOURCE = {
        'name': 'Vox',
        'category': 'business',
        'url': 'https://www.vox.com',
    }

    FEED_URL = 'https://www.vox.com/rss/business-and-finance/index.xml'
