from bs4 import BeautifulSoup
import feedparser
import time

from sources import Source


class UsaTodaySource(Source):

    '''
    Custom feed parser Source for USA Today articles.
    '''

    def update(self):
        feed = feedparser.parse(self.FEED_URL)
        entries = feed['entries']
        for entry in reversed(entries):
            url = entry['link']
            if url in self.stream:
                continue
            update = {}
            update['url'] = url
            update['title'] = clean_html(entry['title'])
            update['body'] = clean_html(entry['summary'])
            if 'media_thumbnail' in entry and len(entry['media_thumbnail']) > 0:
                update['thumb'] = entry['media_thumbnail'][0]['url']
            elif 'media_content' in entry and len(entry['media_content']) > 0:
                update['thumb'] = entry['media_content'][0]['url']
            else:
                thumb = _extract_thumb(entry)
                if thumb:
                    update['thumb'] = thumb
            raw_date = entry['published_parsed']
            update['date'] = time.strftime('%Y-%m-%d %H:%M:%S', raw_date)
            update['source'] = self.SOURCE
            self.stream.push(update)


def clean_html(raw):
    raw = raw.replace('&quot;', '"').replace('&apos;', "'")
    return BeautifulSoup(raw, 'html.parser').get_text().strip()

def _extract_thumb(entry):
    soup = BeautifulSoup(entry['summary'], 'html.parser')
    a = soup.find('a', {'title': "View image"})
    if a:
        href = a['href']
        return href if '.jpg' in href.lower() else None
    else:
        return None