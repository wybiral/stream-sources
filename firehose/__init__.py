import importlib
import os
import time

from stream import Stream


class Firehose:

    '''
    A Firehose manages all stream sources. Once started it will update them
    forever, pushing out their content to any stream they're attached to.
    '''

    def __init__(self, delay=30.0):
        self._delay = delay
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
                continue

    def start(self):
        ''' Start the firehose. '''
        while True:
            self.update()
            time.sleep(self._delay)
