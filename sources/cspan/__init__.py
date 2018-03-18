import requests
from bs4 import BeautifulSoup
from sources import Source as SourceBase


class Source(SourceBase):

    SOURCE = {'name': 'C-SPAN', 'url': 'https://www.c-span.org'}

    def update(self):
        videos = self._recent_videos()
        for video in reversed(videos):
            text = video.find('div', {'class': 'text'})
            url = text.find('a', {'class': 'title'})['href']
            if url in self.stream:
                continue
            update = self._extract_video(video)
            if update is None:
                continue
            self.stream.push(update)

    def _recent_videos(self):
        url = 'https://www.c-span.org/search/'
        query = 'searchtype=Videos&sort=Most+Recent+Airing&ajax&page=1'
        r = requests.get(url + '?' + query)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup.find_all('li', {'class': 'onevid'})

    def _extract_video(self, video):
        update = {}
        text = video.find('div', {'class': 'text'})
        title_a = text.find('a', {'class': 'title'})
        url = title_a['href']
        update['url'] = url
        update['title'] = title_a.find('h3').get_text()
        dates = text.find_all('time')
        date = ''
        if len(dates) > 0 and 'datetime' not in dates[-1]:
            date = dates[-1]['datetime']
        update['date'] = date
        body_p = text.find('p', {'class': 'abstract'})
        if body_p:
            update['body'] = body_p.get_text()
        thumb_a = video.find('a', {'class': 'thumb'})
        update['thumb'] = thumb_a.find_all('img')[0]['src']
        update['source'] = self.SOURCE
        return update
