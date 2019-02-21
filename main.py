import importlib
import os
import time

from stream import Stream


class Firehose:

    '''
    A Firehose manages all stream sources. Once started it will update them
    forever, pushing out their content to any stream they're attached to.
    '''

    # Seconds to sleep between each round of scraping
    DELAY = 30.0

    def __init__(self):
        self._sources = []

    def add_source(self, name, stream=None):
        ''' Add source by name (with optional log stream). '''
        module = importlib.import_module('sources.' + name)
        # If no log stream is supplied one will be created
        if stream is None:
            os.makedirs('logs', exist_ok=True)
            stream = Stream(log_path=os.path.join('logs', name + '.txt'))
        source = module.Source(stream)
        self._sources.append(source)
        return source

    def update(self):
        ''' Update all sources. '''
        for source in self._sources:
            try:
                source.update()
            except Exception as e:
                print(e)
                continue

    def start(self):
        ''' Start the firehose. '''
        while True:
            self.update()
            time.sleep(self.DELAY)


def main():
    firehose = Firehose()
    # Add Ars Technica
    stream = firehose.add_source('arstechnica').stream
    firehose.add_source('arstechnica.business', stream=stream)
    firehose.add_source('arstechnica.gadgets', stream=stream)
    firehose.add_source('arstechnica.science', stream=stream)
    firehose.add_source('arstechnica.security', stream=stream)
    firehose.add_source('arstechnica.software', stream=stream)
    # Add BBC News
    stream = firehose.add_source('bbc').stream
    firehose.add_source('bbc.business', stream=stream)
    firehose.add_source('bbc.science', stream=stream)
    firehose.add_source('bbc.technology', stream=stream)
    firehose.add_source('bbc.world', stream=stream)
    # Add BleepingComputer
    firehose.add_source('bleepingcomputer')
    # Add C-SPAN
    firehose.add_source('cspan')
    # Add HuffPost
    stream = firehose.add_source('huffpost').stream
    firehose.add_source('huffpost.business', stream=stream)
    firehose.add_source('huffpost.politics', stream=stream)
    firehose.add_source('huffpost.science', stream=stream)
    firehose.add_source('huffpost.technology', stream=stream)
    firehose.add_source('huffpost.us', stream=stream)
    firehose.add_source('huffpost.world', stream=stream)
    # Add Krebs on Security
    firehose.add_source('krebsonsecurity')
    # Add NPR News
    stream = firehose.add_source('npr').stream
    firehose.add_source('npr.business', stream=stream)
    firehose.add_source('npr.politics', stream=stream)
    firehose.add_source('npr.science', stream=stream)
    firehose.add_source('npr.technology', stream=stream)
    firehose.add_source('npr.world', stream=stream)
    # Add Reuters
    stream = firehose.add_source('reuters').stream
    firehose.add_source('reuters.business', stream=stream)
    firehose.add_source('reuters.money', stream=stream)
    firehose.add_source('reuters.politics', stream=stream)
    firehose.add_source('reuters.science', stream=stream)
    firehose.add_source('reuters.technology', stream=stream)
    firehose.add_source('reuters.us', stream=stream)
    firehose.add_source('reuters.world', stream=stream)
    # Add Threatpost
    firehose.add_source('threatpost')
    # Add Washington Post
    stream = firehose.add_source('washingtonpost').stream
    firehose.add_source('washingtonpost.business', stream=stream)
    firehose.add_source('washingtonpost.national', stream=stream)
    firehose.add_source('washingtonpost.politics', stream=stream)
    firehose.add_source('washingtonpost.technology', stream=stream)
    firehose.add_source('washingtonpost.world', stream=stream)
    # Start firehose
    firehose.start()


if __name__ == '__main__':
    main()