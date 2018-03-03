import json
import sys

class Stream:

    LOG_SIZE = 100

    def __init__(self, log_path='log.txt'):
        self.log_path = log_path
        self.__log = self.__load_log()
        self.out = sys.stdout

    def __load_log(self):
        try:
            return json.loads(open(self.log_path).read())
        except:
            pass
        return []

    def __save_log(self):
        open(self.log_path, 'w').write(json.dumps(self.__log))

    def __contains__(self, url):
        return url in self.__log

    def push(self, item):
        print(json.dumps(item), file=self.out)
        self.__log.append(item['url'])
        if len(self.__log) >= self.LOG_SIZE:
            self.__log = self.__log[-self.LOG_SIZE:]
        self.__save_log()
