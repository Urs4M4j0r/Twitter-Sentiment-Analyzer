
def writeData(score, date, term):
    f = open("data.txt", "a")
    f.write('\n' + term + ' - ' + score + ':' + date)
    f.close()

#writeData('score', 'date')
