import twitter
import urllib.parse
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import urllib.parse
from collections import defaultdict


analyser = SentimentIntensityAnalyzer()
api = twitter.Api(consumer_key='yWQkZaRBw2AUgf93kgxIOxPqi',
                  consumer_secret='KFs3Q2IkC8RCe2BIWpTSbMYjlaX72lEBeeo94KhEyMkddXag4o',
                  access_token_key='844232093840359424-rfkNbuSbds6VIdWxkLSJvKE3D7fWg4D',
                  access_token_secret='71VDU0qVSAOH9ftz3COELgyVSVnw4KHlpbpKtkQdQ1ex4')



def runNewsAssessment(text):
    return analyser.polarity_scores(text)['compound']


    
def assess_sentiment(tweets):
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
        '''
        if float(analyser.polarity_scores(statement)['compound']) > 0.05:
            pos = pos + 1
        elif float(analyser.polarity_scores(statement)['compound']) < -0.05:
            neg = neg + 1
        else:
            neu = neu + 1
        '''
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
        #graph.createGraph(pos, neu, neg)
        #print(i)
        
    totalAvgTB = totalTB / len(tweets)
    totalAvgVader = totalVader / len(tweets)
    return totalAvgVader, totalAvgTB, pos, neu, neg, vpos, spos, sneg, vneg

def urlEncode(term):
    termURL = urllib.parse.quote(term)
    return termURL

def createSearch(term, searchType, dateStart, numTweetToShow):
    try:
        x = int(numTweetToShow)
    except Exception as ex:
        numTweetToShow = str("5")
        
    #termURL = urllib.parse.quote(term)
    termURL = urlEncode(term)
    searchString = "q=" + termURL + "&result_type=" + searchType + "&return_json=true&lang=en&tweet_mode=extended&since=" + dateStart + "&count=" + numTweetToShow
    results = api.GetSearch(raw_query=searchString)
    avgSentiment = assess_sentiment(results)
    return avgSentiment
