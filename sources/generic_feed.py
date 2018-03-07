from bs4 import BeautifulSoup
import feedparser
import time

def create_update(feed_url, source):
    def update(stream):
        feed = feedparser.parse(feed_url)
        entries = feed['entries']
        for entry in reversed(entries):
            url = entry['link']
            if url in stream:
                continue
            update = {}
            update['url'] = url
            update['title'] = clean_html(entry['title'])
            update['body'] = clean_html(entry['summary'])
            if 'media_content' in entry and len(entry['media_content']) > 0:
                update['thumb'] = entry['media_content'][0]['url']
            else:
                thumb = __extract_thumb(entry)
                if thumb:
                    update['thumb'] = thumb
            raw_date = entry['published_parsed']
            update['date'] = time.strftime('%Y-%m-%d %H:%M:%S', raw_date)
            update['source'] = source
            stream.push(update)
    return update

def clean_html(raw):
    return BeautifulSoup(raw, 'html.parser').get_text().strip()

def __extract_thumb(entry):
    if 'content' not in entry:
        return None
    if len(entry.content) < 1:
        return None
    content = entry.content[0]
    if 'value' not in content:
        return None
    soup = BeautifulSoup(content['value'], 'html.parser')
    img = soup.find('img')
    if img:
        return img['src']
    return None
