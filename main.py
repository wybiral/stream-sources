import os
import time
import importlib
from stream import Stream


class Firehose:

    DELAY = 60.0

    def __init__(self):
        self.sources = []

    def add_source(self, name, stream=None):
        module = importlib.import_module('sources.' + name)
        if stream is None:
            os.makedirs('logs', exist_ok=True)
            stream = Stream(os.path.join('logs', name + '.txt'))
        source = module.Source(stream)
        self.sources.append(source)
        return source

    def update(self):
        for source in self.sources:
            source.update()

    def run(self):
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
    # Add Krebs on Security
    firehose.add_source('krebsonsecurity')
    # Add NPR News
    stream = firehose.add_source('npr').stream
    firehose.add_source('npr.business', stream=stream)
    firehose.add_source('npr.politics', stream=stream)
    firehose.add_source('npr.science', stream=stream)
    firehose.add_source('npr.technology', stream=stream)
    firehose.add_source('npr.world', stream=stream)
    # Add Radware advisories
    firehose.add_source('radware.advisories')
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
    # Run firehose
    firehose.run()


if __name__ == '__main__':
    main()