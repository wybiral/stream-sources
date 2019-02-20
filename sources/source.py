from stream import Stream


class Source:

    '''
    A Source implements an .update() method which scrapes articles from a single
    source and pushes them to a Stream.
    '''

    def __init__(self, stream=None):
        if stream is None:
            stream = Stream()
        self.stream = stream

    def update(self):
        raise NotImplementedError
