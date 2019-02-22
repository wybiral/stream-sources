from sources.vox._source import VoxSource


class Source(VoxSource):

    SOURCE = {
        'name': 'Vox',
        'category': 'technology',
        'url': 'https://www.vox.com',
    }

    FEED_URL = 'https://www.vox.com/rss/technology/index.xml'
