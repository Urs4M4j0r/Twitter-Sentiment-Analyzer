import twitter
import urllib.parse
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import urllib.parse
from collections import defaultdict
import configparser

analyser = SentimentIntensityAnalyzer()
Config = configparser.ConfigParser()
Config.read("config.ini")
cfgfile = open("config.ini", 'r')


api = twitter.Api(consumer_key=Config.get('APIKeys', 'consumerkey'),
                  consumer_secret=Config.get('APIKeys', 'consumersecret'),
                  access_token_key=Config.get('APIKeys', 'accesstokenkey'),
                  access_token_secret=Config.get('APIKeys', 'accesstokensecret'))

    
def assess_sentiment(tweets):
    divzero = False
    spos = 0
    pos = 0
    vpos = 0
    neu = 0
    sneg = 0
    neg = 0
    vneg = 0
    totalVader = 0
    totalTB = 0
    for i in tweets:
        resultsString = i.full_text
        statement = resultsString
        totalVader = totalVader + analyser.polarity_scores(statement)['compound']
        totalTB = totalTB + TextBlob(statement).sentiment.polarity
        score = float(analyser.polarity_scores(statement)['compound'])
        
        if score < 0.05 and score > -0.05:
            neu += 1
        elif score < -0.05 and score > -0.3:
            sneg += 1
        elif score < -0.3 and score > -0.9:
            neg += 1
        elif score < -0.9:
            vneg += 1
        elif score > 0.05 and score < 0.3:
            spos += 1
        elif score > 0.3 and score < 0.9:
            pos += 1
        elif score > 0.9:
            vpos += 1
            
    try:    
        totalAvgTB = totalTB / len(tweets)
        totalAvgVader = totalVader / len(tweets)
    except ZeroDivisionError:
        divzero = True
        

    return totalAvgVader, totalAvgTB, pos, neu, neg, vpos, spos, sneg, vneg, divzero

def urlEncode(term):
    termURL = urllib.parse.quote(term)
    return termURL

def createSearch(term, searchType, dateStart, numTweetToShow):
    try:
        x = int(numTweetToShow)
    except Exception as ex:
        numTweetToShow = str("5")
        
    termURL = urlEncode(term)
    searchString = "q=" + termURL + "&result_type=" + searchType + "&return_json=true&lang=en&tweet_mode=extended&since=" + dateStart + "&count=" + numTweetToShow
    results = api.GetSearch(raw_query=searchString)
    avgSentiment = assess_sentiment(results)
    return avgSentiment
