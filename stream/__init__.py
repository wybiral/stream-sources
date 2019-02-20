import json
import sys

class Stream:

    '''
    A Stream is responsible for writing items to stdout and caching their URLs
    in a log file so Sources can avoid pushing duplicates.

    Multiple sources should share a stream if they contain duplicates. For
    instance Top News and World News categories from the same news source may
    contain the same articles and should share the same stream.
    '''

    # Maximum number of recent log entries to store
    LOG_SIZE = 500

    def __init__(self, out=sys.stdout, log_path='log.txt'):
        self.out = out
        self.log_path = log_path
        self.__log = self.__load_log()

    def __load_log(self):
        ''' Load log file from log_path. '''
        try:
            return open(self.log_path).read().split('\n')
        except:
            pass
        return []

    def __save_log(self):
        ''' Save log file to log_path. '''
        open(self.log_path, 'w').write('\n'.join(self.__log))

    def __contains__(self, url):
        ''' Check if url is in log. '''
        return url in self.__log

    def push(self, item):
        ''' Push JSON encoded item to output and append URL to log. '''
        json.dump(item, self.out)
        self.out.write('\n')
        self.out.flush()
        self.__log.append(item['url'])
        if len(self.__log) >= self.LOG_SIZE:
            self.__log = self.__log[-self.LOG_SIZE:]
        self.__save_log()
