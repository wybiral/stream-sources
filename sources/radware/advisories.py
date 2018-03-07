import requests
from bs4 import BeautifulSoup

SOURCE = {
    'name': 'Radware (Advisories)',
    'url': 'https://security.radware.com/'
}

def update(stream):
    updates = __recent_updates()
    for x in reversed(updates):
        title = x.find('h2', {'class': 'article-title'})
        url = title.find('a')['href']
        url = 'https://security.radware.com' + url
        if url in stream:
            continue
        update = {}
        update['title'] = title.get_text().strip()
        update['url'] = url
        date = x.find('div', {'class': 'date-issued'}).get_text().strip()
        parts = date.split('/')
        year = int(parts[2])
        month = int(parts[0])
        day = int(parts[1])
        date = '%4d-%02d-%02d' % (year, month, day)
        update['date'] = date
        update['source'] = SOURCE
        media_body = x.find('div', {'class': 'media-body'})
        update['body'] = media_body.find('p').get_text().strip()
        stream.push(update)

def __recent_updates():
    base = 'https://security.radware.com'
    path = 'ddos-threats-attacks/threat-advisories-attack-reports'
    r = requests.get(base + '/' + path)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all('div', {'class': 'media'})
