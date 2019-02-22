from sources.vox._source import VoxSource


class Source(VoxSource):

    SOURCE = {
        'name': 'Vox',
        'category': 'politics',
        'url': 'https://www.vox.com',
    }

    FEED_URL = 'https://www.vox.com/rss/policy-and-politics/index.xml'
