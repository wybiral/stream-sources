from bs4 import BeautifulSoup
import feedparser
import time

from sources import Source


class FeedSource(Source):

    '''
    A generic FeedSource baseclass implements a Source class for RSS feeds.

    Classes that inherit from FeedSource should have their own FEED_URL (an RSS
    feed URL) and SOURCE (the source name) class properties.
    '''

    def update(self):
        feed = feedparser.parse(self.FEED_URL)
        entries = feed['entries']
        for entry in reversed(entries):
            url = entry['link']
            if url in self.stream:
                continue
            if not self.filter(entry):
                continue
            update = {}
            update['url'] = url
            update['title'] = clean_html(entry['title'])
            update['body'] = clean_html(_extract_body(entry))
            thumb = _extract_thumb(entry)
            if thumb:
                update['thumb'] = thumb
            raw_date = entry['published_parsed']
            update['date'] = time.strftime('%Y-%m-%d %H:%M:%S', raw_date)
            update['source'] = self.SOURCE
            self.stream.push(update)

    def filter(self, entry):
        return True


def clean_html(raw):
    return BeautifulSoup(raw, 'html.parser').get_text().strip()

def _extract_body(entry):
    texts = []
    texts.append(entry['summary'])
    # some publications put the whole article so we search for the true summary
    # by looking for the shortest text/html content if multiple exist.
    if 'content' in entry:
        for content in entry['content']:
            if content['type'] == 'text/html':
                texts.append(content['value'])
    texts.sort(key=lambda x: len(x))
    return texts[0]

def _extract_thumb(entry):
    if 'media_thumbnail' in entry and len(entry['media_thumbnail']) > 0:
        return entry['media_thumbnail'][0]['url']
    if 'media_content' in entry and len(entry['media_content']) > 0:
        return entry['media_content'][0]['url']
    if 'links' in entry and len(entry['links']) > 0:
        imgs = [x for x in entry['links'] if 'image' in x['type']]
        if len(imgs) > 0:
            return imgs[0]['href']
    soup = BeautifulSoup(entry['summary'], 'html.parser')
    img = soup.find('img')
    if img:
        return img['src']
    return None
