import numpy as np
import matplotlib.pyplot as plt
 

def createGraph(pos, neu, neg, date, spos, vpos, sneg, vneg, term):
    
    # creating the dataset
    positive = 'Positive: ' + str(pos)
    spositive = 'Slightly Positive: ' + str(spos)
    vpositive = ' Very Positive: ' + str(vpos)
    neutral = 'Neutral: ' + str(neu)
    negative = 'Negative: ' + str(neg)
    snegative = 'Slightly Negative: ' + str(sneg)
    vnegative = 'Very Negative: ' + str(vneg)
    #data = {positive:pos, neutral:neu, negative:neg}
    data = {vnegative:vneg, negative:neg, snegative:sneg, neutral:neu, spositive:spos, positive:pos, vpositive:vpos}
    courses = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize = (12, 5))
    # creating the bar plot
    plt.bar(courses, values, color ='black',
        width = 0.4)
    plt.title("Tweet Sentiment Count - " + term + " - " + str(date))
    plt.show()
