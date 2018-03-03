import requests
from bs4 import BeautifulSoup

SOURCE = {'name': 'C-SPAN', 'url': 'https://www.c-span.org'}

def update(stream):
    videos = __recent_videos()
    for video in reversed(videos):
        text = video.find('div', {'class': 'text'})
        url = text.find('a', {'class': 'title'})['href']
        if url in stream:
            continue
        update = __extract_video(video)
        stream.push(update)

def __recent_videos():
    url = 'https://www.c-span.org/search/'
    query = 'searchtype=Videos&sort=Most+Recent+Airing&ajax&page=1'
    r = requests.get(url + '?' + query)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all('li', {'class': 'onevid'})

def __extract_video(video):
    update = {}
    text = video.find('div', {'class': 'text'})
    title_a = text.find('a', {'class': 'title'})
    url = title_a['href']
    update['url'] = url
    update['title'] = title_a.find('h3').get_text()
    dates = text.find_all('time')
    update['date'] = dates[1]['datetime']
    body_p = text.find('p', {'class': 'abstract'})
    if body_p:
        update['body'] = body_p.get_text()
    thumb_a = video.find('a', {'class': 'thumb'})
    update['thumb'] = thumb_a.find_all('img')[0]['src']
    update['source'] = SOURCE
    return update
