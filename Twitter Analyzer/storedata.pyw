
def writeData(score, date):
    f = open("data.txt", "a")
    f.write('\n' + score + ':' + date)
    f.close()

#writeData('score', 'date')
