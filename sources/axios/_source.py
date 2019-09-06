from bs4 import BeautifulSoup
from sources.generic import FeedSource


class AxiosSource(FeedSource):

    '''
    Custom feed parser Source for Axios articles.
    '''

    def clean_body(self, body):
        s = BeautifulSoup(body, 'html.parser')
        p = s.find_all('p')
        return p[0].get_text().strip()
