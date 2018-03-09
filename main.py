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
    source = firehose.add_source('arstechnica')
    firehose.add_source('arstechnica.business', stream=source.stream)
    firehose.add_source('arstechnica.gadgets', stream=source.stream)
    firehose.add_source('arstechnica.science', stream=source.stream)
    firehose.add_source('arstechnica.security', stream=source.stream)
    firehose.add_source('arstechnica.software', stream=source.stream)
    # Add BleepingComputer
    firehose.add_source('bleepingcomputer')
    # Add C-SPAN
    firehose.add_source('cspan')
    # Add Krebs on Security
    firehose.add_source('krebsonsecurity')
    # Add Radware advisories
    firehose.add_source('radware.advisories')
    # Add Reuters
    source = firehose.add_source('reuters')
    firehose.add_source('reuters.business', stream=source.stream)
    firehose.add_source('reuters.money', stream=source.stream)
    firehose.add_source('reuters.politics', stream=source.stream)
    firehose.add_source('reuters.science', stream=source.stream)
    firehose.add_source('reuters.technology', stream=source.stream)
    firehose.add_source('reuters.us', stream=source.stream)
    firehose.add_source('reuters.world', stream=source.stream)
    # Add Threatpost
    firehose.add_source('threatpost')
    # Add Washington Post
    source = firehose.add_source('washingtonpost')
    firehose.add_source('washingtonpost.business', stream=source.stream)
    firehose.add_source('washingtonpost.national', stream=source.stream)
    firehose.add_source('washingtonpost.politics', stream=source.stream)
    firehose.add_source('washingtonpost.technology', stream=source.stream)
    firehose.add_source('washingtonpost.world', stream=source.stream)
    # Run firehose
    firehose.run()


if __name__ == '__main__':
    main()