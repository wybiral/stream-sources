from stream import Stream


class Source:

    def __init__(self, stream=None):
        if stream is None:
            stream = Stream()
        self.stream = stream

    def update(self):
        raise NotImplementedError