from firehose import Firehose


def main():
    firehose = Firehose()
    # Add ABC News
    stream = firehose.add_source('abc.politics').stream
    firehose.add_source('abc.technology', stream=stream)
    firehose.add_source('abc.us', stream=stream)
    firehose.add_source('abc.world', stream=stream)
    firehose.add_source('abc', stream=stream)
    # Add Ars Technica
    stream = firehose.add_source('arstechnica.business').stream
    firehose.add_source('arstechnica.gadgets', stream=stream)
    firehose.add_source('arstechnica.science', stream=stream)
    firehose.add_source('arstechnica.security', stream=stream)
    firehose.add_source('arstechnica.software', stream=stream)
    firehose.add_source('arstechnica', stream=stream)
    # Add BBC News
    stream = firehose.add_source('bbc.business').stream
    firehose.add_source('bbc.science', stream=stream)
    firehose.add_source('bbc.technology', stream=stream)
    firehose.add_source('bbc.world', stream=stream)
    firehose.add_source('bbc', stream=stream)
    # Add BleepingComputer
    firehose.add_source('bleepingcomputer')
    # Add BuzzFeed News
    stream = firehose.add_source('buzzfeednews.politics').stream
    firehose.add_source('buzzfeednews.technology', stream=stream)
    firehose.add_source('buzzfeednews.world', stream=stream)
    firehose.add_source('buzzfeednews', stream=stream)
    # Add CNBC
    stream = firehose.add_source('cnbc.business').stream
    firehose.add_source('cnbc.politics', stream=stream)
    firehose.add_source('cnbc.technology', stream=stream)
    firehose.add_source('cnbc.us', stream=stream)
    firehose.add_source('cnbc.world', stream=stream)
    firehose.add_source('cnbc', stream=stream)
    # Add C-SPAN
    firehose.add_source('cspan')
    # Add HuffPost
    stream = firehose.add_source('huffpost.business').stream
    firehose.add_source('huffpost.politics', stream=stream)
    firehose.add_source('huffpost.science', stream=stream)
    firehose.add_source('huffpost.technology', stream=stream)
    firehose.add_source('huffpost.us', stream=stream)
    firehose.add_source('huffpost.world', stream=stream)
    firehose.add_source('huffpost', stream=stream)
    # Add Krebs on Security
    firehose.add_source('krebsonsecurity')
    # Add NPR News
    stream = firehose.add_source('npr.business').stream
    firehose.add_source('npr.politics', stream=stream)
    firehose.add_source('npr.science', stream=stream)
    firehose.add_source('npr.technology', stream=stream)
    firehose.add_source('npr.world', stream=stream)
    firehose.add_source('npr', stream=stream)
    # Add Politico
    stream = firehose.add_source('politico.congress').stream
    firehose.add_source('politico.defense', stream=stream)
    firehose.add_source('politico.economy', stream=stream)
    firehose.add_source('politico', stream=stream)
    # Add Reuters
    stream = firehose.add_source('reuters.business').stream
    firehose.add_source('reuters.money', stream=stream)
    firehose.add_source('reuters.politics', stream=stream)
    firehose.add_source('reuters.science', stream=stream)
    firehose.add_source('reuters.technology', stream=stream)
    firehose.add_source('reuters.us', stream=stream)
    firehose.add_source('reuters.world', stream=stream)
    firehose.add_source('reuters', stream=stream)
    # Add The Atlantic
    stream = firehose.add_source('theatlantic.business').stream
    firehose.add_source('theatlantic.politics', stream=stream)
    firehose.add_source('theatlantic.science', stream=stream)
    firehose.add_source('theatlantic.technology', stream=stream)
    firehose.add_source('theatlantic.us', stream=stream)
    firehose.add_source('theatlantic', stream=stream)
    # Add The Guardian
    stream = firehose.add_source('theguardian.business').stream
    firehose.add_source('theguardian.politics', stream=stream)
    firehose.add_source('theguardian.science', stream=stream)
    firehose.add_source('theguardian.technology', stream=stream)
    firehose.add_source('theguardian.us', stream=stream)
    firehose.add_source('theguardian.world', stream=stream)
    firehose.add_source('theguardian', stream=stream)
    # Add The Hill
    stream = firehose.add_source('thehill.administration').stream
    firehose.add_source('thehill.house', stream=stream)
    firehose.add_source('thehill.senate', stream=stream)
    firehose.add_source('thehill', stream=stream)
    # Add Threatpost
    firehose.add_source('threatpost')
    '''
    # Add USA Today
    stream = firehose.add_source('usatoday.national').stream
    firehose.add_source('usatoday.washington', stream=stream)
    firehose.add_source('usatoday.world', stream=stream)
    firehose.add_source('usatoday', stream=stream)
    '''
    # Add Vox
    stream = firehose.add_source('vox.business').stream
    firehose.add_source('vox.politics', stream=stream)
    firehose.add_source('vox.technology', stream=stream)
    firehose.add_source('vox.world', stream=stream)
    firehose.add_source('vox', stream=stream)
    # Add Washington Post
    stream = firehose.add_source('washingtonpost.business').stream
    firehose.add_source('washingtonpost.national', stream=stream)
    firehose.add_source('washingtonpost.politics', stream=stream)
    firehose.add_source('washingtonpost.technology', stream=stream)
    firehose.add_source('washingtonpost.world', stream=stream)
    firehose.add_source('washingtonpost', stream=stream)
    # Add Wired
    stream = firehose.add_source('wired.business').stream
    firehose.add_source('wired.science', stream=stream)
    firehose.add_source('wired.security', stream=stream)
    firehose.add_source('wired', stream=stream)
    # Start firehose
    firehose.start()


if __name__ == '__main__':
    main()