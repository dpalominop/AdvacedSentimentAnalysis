__author__ = 'Daniel Palomino'

import xml.etree.ElementTree as ET
import Tweet as tw


def readXML(xmlFIle):
    tree = ET.parse(xmlFIle)
    root = tree.getroot()

    tweets = []
    
    for tweet in root.iter('tweet'):
        content = tweet.find('content').text
        sentiment = tweet.find('sentiment')
        polarity = sentiment.find('polarity').find('value').text
        polarity = treeLevels(polarity)
        
        # Other info:
        
        tweet_id = int(tweet.find('tweetid').text)
        user = tweet.find('user').text
        date = tweet.find('date').text
        lang = tweet.find('lang').text
        
        if content != None:
            tweet = tw.Tweet(tweet_id, user, date, lang, content, polarity)
            tweets.append(tweet)

    return tweets


def readXMLTest(xmlFIle):
    tree = ET.parse(xmlFIle)
    root = tree.getroot()

    tweets = []

    for tweet in root.iter('tweet'):
        content = tweet.find('content').text

        # sentiments = tweet.find('sentiments')
        # polarity = sentiments[0].find('value').text
        polatity = 'NONE'
        # polarity = polarityTagging(polarity)

        # Other info:
        tweet_id = tweet.find('tweetid').text
        user = tweet.find('user').text
        date = tweet.find('date').text
        lang = tweet.find('lang').text

        if content != None:
            tweet = tw.Tweet(tweet_id, user, date, lang, content, polatity)
            tweets.append(tweet)

    return tweets

def treeLevels(polarity):

    if   (polarity.__eq__('N') ):
        polarity = 0
    elif (polarity.__eq__('N+')):
        polarity = 0
    elif (polarity.__eq__('P') ):
        polarity = 1
    elif (polarity.__eq__('P+')):
        polarity = 1
    elif (polarity.__eq__('NEU')):
        polarity = 2
    elif (polarity.__eq__('NONE')):
        polarity = 2

    return polarity