import requests
import nlp

def pullNewsStories(term, date):
    term2 = str(term)
    term3 = nlp.urlEncode(term2)
    date2 = str(date)
    avgScore = 0
    urlText = 'https://newsapi.org/v2/everything?qInTitle=' + term2 + '&language=en&from=' + date2 + '&to=' + date2 + '&sortBy=popularity&apiKey=e07f9ca20a004526bb44088fe9490ee4'
    url = urlText
    response = requests.get(url)
    r = response.json()
    r2 = r.get('articles')
    for i in r2:
        text = i.get('title')
        avgScore = avgScore + float(nlp.runNewsAssessment(text))
    if len(r2) == 0:
        average = avgScore
    else:
        average = avgScore / len(r2)
    return average
