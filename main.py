from firehose import Firehose


def main():
    firehose = Firehose()
    # Add ABC News
    stream = firehose.add_source('abc').stream
    firehose.add_source('abc.politics', stream=stream)
    firehose.add_source('abc.technology', stream=stream)
    firehose.add_source('abc.us', stream=stream)
    firehose.add_source('abc.world', stream=stream)
    # Add Ars Technica
    stream = firehose.add_source('arstechnica').stream
    firehose.add_source('arstechnica.business', stream=stream)
    firehose.add_source('arstechnica.gadgets', stream=stream)
    firehose.add_source('arstechnica.science', stream=stream)
    firehose.add_source('arstechnica.security', stream=stream)
    firehose.add_source('arstechnica.software', stream=stream)
    # Add BBC News
    stream = firehose.add_source('bbc').stream
    firehose.add_source('bbc.business', stream=stream)
    firehose.add_source('bbc.science', stream=stream)
    firehose.add_source('bbc.technology', stream=stream)
    firehose.add_source('bbc.world', stream=stream)
    # Add BleepingComputer
    firehose.add_source('bleepingcomputer')
    # Add CNBC
    stream = firehose.add_source('cnbc').stream
    firehose.add_source('cnbc.business', stream=stream)
    firehose.add_source('cnbc.politics', stream=stream)
    firehose.add_source('cnbc.technology', stream=stream)
    firehose.add_source('cnbc.us', stream=stream)
    firehose.add_source('cnbc.world', stream=stream)
    # Add C-SPAN
    firehose.add_source('cspan')
    # Add HuffPost
    stream = firehose.add_source('huffpost').stream
    firehose.add_source('huffpost.business', stream=stream)
    firehose.add_source('huffpost.politics', stream=stream)
    firehose.add_source('huffpost.science', stream=stream)
    firehose.add_source('huffpost.technology', stream=stream)
    firehose.add_source('huffpost.us', stream=stream)
    firehose.add_source('huffpost.world', stream=stream)
    # Add Krebs on Security
    firehose.add_source('krebsonsecurity')
    # Add NPR News
    stream = firehose.add_source('npr').stream
    firehose.add_source('npr.business', stream=stream)
    firehose.add_source('npr.politics', stream=stream)
    firehose.add_source('npr.science', stream=stream)
    firehose.add_source('npr.technology', stream=stream)
    firehose.add_source('npr.world', stream=stream)
    # Add Politico
    stream = firehose.add_source('politico').stream
    firehose.add_source('politico.congress', stream=stream)
    firehose.add_source('politico.defense', stream=stream)
    firehose.add_source('politico.economy', stream=stream)
    # Add Reuters
    stream = firehose.add_source('reuters').stream
    firehose.add_source('reuters.business', stream=stream)
    firehose.add_source('reuters.money', stream=stream)
    firehose.add_source('reuters.politics', stream=stream)
    firehose.add_source('reuters.science', stream=stream)
    firehose.add_source('reuters.technology', stream=stream)
    firehose.add_source('reuters.us', stream=stream)
    firehose.add_source('reuters.world', stream=stream)
    # Add Threatpost
    firehose.add_source('threatpost')
    # Add Washington Post
    stream = firehose.add_source('washingtonpost').stream
    firehose.add_source('washingtonpost.business', stream=stream)
    firehose.add_source('washingtonpost.national', stream=stream)
    firehose.add_source('washingtonpost.politics', stream=stream)
    firehose.add_source('washingtonpost.technology', stream=stream)
    firehose.add_source('washingtonpost.world', stream=stream)
    # Start firehose
    firehose.start()


if __name__ == '__main__':
    main()