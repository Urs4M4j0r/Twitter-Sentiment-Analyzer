from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import nlp
from datetime import date
import graph
import newsAnalysis
import storedata
import configparser



def measureText(sentScore):
    scoreDescription = "None"
    if float(sentScore) < 0.05 and float(sentScore) > -0.05:
        scoreDescription = "(Neutral)"
    elif float(sentScore) < -0.05 and float(sentScore) > -0.3:
        scoreDescription = "(Slightly Bad)"
    elif float(sentScore) < -0.3 and float(sentScore) > -0.9:
        scoreDescription = "(Bad)"
    elif float(sentScore) < -0.9:
        scoreDescription = "(Very Bad)"
    elif float(sentScore) > 0.05 and float(sentScore) < 0.3:
        scoreDescription = "(Slightly Good)"
    elif float(sentScore) > 0.3 and float(sentScore) < 0.9:
        scoreDescription = "(Good)"
    elif float(sentScore) > 0.9:
        scoreDescription = "(Very Good)"
        
    return scoreDescription



def analyzeNews():
    avgnews = newsAnalysis.pullNewsStories(searchTermText.get(), date.today())
    if avgnews == 0:
        newsText = "No news stories found."
    else:
        avgnewsText = str(avgnews)
        newsText = "News sentiment for " + str(date.today()) + " is " + avgnewsText[0:5] + " " + measureText(avgnews)
    updateMessage(newsText)



def g(pos, neu, neg, spos, vpos, sneg, vneg):
    g.pos = int(pos)
    g.neu = int(neu)
    g.neg = int(neg)
    g.spos = int(spos)
    g.vpos = int(vpos)
    g.sneg = int(sneg)
    g.vneg = int(vneg)



def printGraph():
    dateToUse = "Error"
    if todaySelector.get() == 1:
        dateToUse = str(date.today())
    else:
        dateToUse = searchDateText.get()
    graph.createGraph(g.pos, g.neu, g.neg, dateToUse, g.spos, g.vpos, g.sneg, g.vneg, searchTermText.get())


    
def updateMessage(message):
    outMsg.configure(text=message)



def printSent(sentScoreV, sentScoreTB, outString, selector):
    if selector == 1:
        out = outString + '\n' + '\n' + "Average TextBlob sentiment is: " + sentScoreTB[0:5] + ' ' + measureText(sentScoreTB)
        
    elif selector == 2:
        out = outString + '\n' + '\n' + "Average VADER sentiment is: " + sentScoreV[0:5] + ' ' + measureText(sentScoreV)

    elif selector == 3:
        out = outString + '\n' + '\n' + "Average VADER sentiment is: " + sentScoreV[0:5] + ' ' + measureText(sentScoreV) + '\n' + "Average TextBlob sentiment is: " + sentScoreTB[0:5] + ' ' + measureText(sentScoreTB)
        
    else:
        out = outString + '\n' + '\n' + "Average VADER sentiment is: " + sentScoreV[0:5] + ' ' + measureText(sentScoreV)
        
    '''
    if int(Cryptoselector.get()) == 1:
        out2 = out + '\n' + '\n' + str(selectedCrypto.get()) + ' 24h price change:' + str(cryptopriceapi.getCryptoPriceChange24h(selectedCrypto.get())) + '%'
    else:
        out2 = out
    '''

    dateSel2 = todaySelector.get()
    if dateSel2 == 1:
        datetoprint2 = str(date.today())
    else:
        datetoprint2 = searchDateText.get()
    storedata.writeData(str(sentScoreV[0:5]), datetoprint2, searchTermText.get()) 
    window.after(5000, updateMessage, out2)
    
    

def output():
    usedanalyser = "Undefined"
    selectorNum = 0
    termtoprint=searchTermText.get()
    dateSel = todaySelector.get()
    if dateSel == 1:
        datetoprint = str(date.today())
    else:
        datetoprint=searchDateText.get()
    selectedTypetoprint=selectedType.get()
    if int(numTweets.get()) > 100:
        numTweetstoprint = "100"
        messageOnTweetNum = "Note: Because of Twitter rate limiting number of tweets retrieved was reduced to 100."
    else:
        numTweetstoprint=numTweets.get()
        messageOnTweetNum = ""
    vader = VADERselector.get()
    textblob = TextBlobselector.get()
    if vader == 1 and textblob == 1:
        usedanalyser = "VADER and TextBlob"
        selectorNum = 3
    elif vader == 1 and textblob == 0 :
        usedanalyser = "VADER"
        selectorNum = 2
    elif vader == 0 and textblob == 1:
        usedanalyser = "TextBlob"
        selectorNum = 1
    else:
        usedanalyser = "Default of VADER will be used"

    

    outputAvg = nlp.createSearch(termtoprint, selectedTypetoprint, datetoprint, numTweetstoprint)
    outputAvgVader = str(outputAvg[0])
    outputAvgTB = str(outputAvg[1])
    pos = int(outputAvg[2])
    neu = int(outputAvg[3])
    neg = int(outputAvg[4])
    spos = int(outputAvg[6])
    vpos = int(outputAvg[5])
    sneg = int(outputAvg[7])
    vneg = int(outputAvg[8])
    g(pos, neu, neg, spos, vpos, sneg, vneg)
    #g(pos, neu, neg)
    totalRetrieved = pos + neu + neg
    outString = "Search term: " + termtoprint + '\n' + "Search date: " + datetoprint + '\n' + "Search type: " +selectedTypetoprint + \
                '\n' + "Number of tweets used: " +numTweetstoprint + '\n' + "Analyzer used: " + usedanalyser + '\n' + "Number of Tweets retrieved: " + str(totalRetrieved) + \
                '\n' + '\n' + messageOnTweetNum

    
    window.after(2000, updateMessage, outString)
    averageText = "The sentiment for the given information is: " + outputAvgVader
    printSent(outputAvgVader, outputAvgTB, outString, selectorNum)


    
def exitProgram():
    window.destroy()



def launchHelp():
    helpWindow = Toplevel(window)
    helpWindow.iconbitmap("img.ico")
    helpWindow.title("About")
    helpWindow.geometry("600x400")
    helpText = "Twitter Sentiment Analyzer" + '\n' + "Eric Hooper 05/06/2021" + '\n' + '\n' + "About:" + '\n' + \
                "This program uses the twitter API to pull a defined number of tweets containing a given search term and performs sentiment analysis to give an average score reflecting the overall sentiment of the topic. The sentiment analyzers used utilize pretrained machine learning models."\
                + '\n' + '\n' + "Sentiment Analysis Methods:" +'\n' + \
                "TextBlob - TextBlob is a simple sentiment analyzer which returns a score for polarity as well as subjectivity. This program utilizes only the polarity score which ranges from -1 to 1."\
                + '\n' + "TextBlob Github - https://github.com/sloria/TextBlob" + '\n' + '\n' + \
                "VADER - The Valence Aware Dictionary sEntiment Reasoner (VADER) is an open source sentiment analyzer developed by MIT and specialized in short form (social media) sentiment analysis. VADER also provides scores ranging from -1 to 1."\
                + '\n' + "VADER Github - https://github.com/cjhutto/vaderSentiment" + '\n' + '\n' + \
                "Notes - " + '\n' + "If a non-interger value in entered into the number of tweets to pull a default value of 5 will be used." + \
                '\n' + "Because of Twitter rate limiting a maximum of 100 tweets can be pulled at once." + \
                '\n' + "Sometimes fewer tweets will be retrieved than is specified if the number of results for the search is less than the number entered."

    helpLabel = Label(helpWindow, text=helpText, justify=LEFT, wraplength=550)
    helpLabel.place(x=0,y=0)

def launchEditAPIWindow():
    apiWindow = Toplevel(window)
    apiWindow.iconbitmap("img.ico")
    apiWindow.title("Edit API Key")
    apiWindow.geometry("600x600")

    #Create search date input
    consumerKey = StringVar()
    consumerSecret = StringVar()
    accessTokenKey = StringVar()
    accessTokenSecret = StringVar()
    consumerKeyBox = Entry(apiWindow, width=18, textvariable=consumerKey)
    consumerSecretBox = Entry(apiWindow, width=18, textvariable=consumerSecret)
    accessTokenKeyBox = Entry(apiWindow, width=18, textvariable=accessTokenKey)
    accessTokenSecretBox = Entry(apiWindow, width=18, textvariable=accessTokenSecret)
    
    consumerKeyBox.place(x=25, y=25)
    consumerSecretBox.place(x=25, y=75)
    accessTokenKeyBox.place(x=25, y=125)
    accessTokenSecretBox.place(x=25, y=175)
    
    textlblCK = Label(apiWindow, text="Enter Twitter Consumer Key:")
    textlblCK.place(x=25, y=0)
    textlblCS = Label(apiWindow, text="Enter Twitter Consumer Secret:")
    textlblCS.place(x=25, y=50)
    textlblATK = Label(apiWindow, text="Enter Twitter Access Token Key:")
    textlblATK.place(x=25, y=100)
    textlblATSK = Label(apiWindow, text="Enter Twitter Access Token Secret Key:")
    textlblATSK.place(x=25, y=150)

    setButton = Button(apiWindow, text="Set keys", relief = "groove", height = 1, width = 8, command=lambda: setKeys(consumerKey.get(), consumerSecret.get(), accessTokenKey.get(), accessTokenSecret.get())) #command=openTesterWindow)
    setButton.place(x=25, y=250)
  

    def setKeys(ck, cs, atk, ats):
    
        #Set up config parser
        Config = configparser.ConfigParser()
        Config.read("config.ini")
        cfgfile = open("config.ini", 'w')

        Config.set('APIKeys', 'consumerkey', str(ck))
        Config.set('APIKeys', 'consumersecret', str(cs))
        Config.set('APIKeys', 'accesstokenkey', str(atk))
        Config.set('APIKeys', 'accesstokensecret', str(ats))
        Config.write(cfgfile)
        cfgfile.close()
        if messagebox.showinfo("Set API Keys", "API keys set in config.ini"):
           apiWindow.destroy()
    


window = Tk()
#Sets the windows title
window.title("Twitter Sentiment Analyzer")
#Sets the initial resolution/size of the window
window.geometry('900x600')


#Create search term input
#Creates a text entry widget
searchTermText=StringVar()
searchterm = Entry(window, width=25, textvariable=searchTermText)
#Sets textbox position in the window
searchterm.place(x=250, y=75)
textlbl = Label(window, text="*Enter search term:")
textlbl.place(x=75, y=75)


#Create search date input
searchDateText = StringVar()
searchDate = Entry(window, width=18, textvariable=searchDateText)
searchDate.place(x=250, y=125)
textlblDate = Label(window, text="*Enter starting search date:")
textlblDate.place(x=75, y=125)

#Add a today checkbox
todaySelector = IntVar()
todayButton = Checkbutton(window, width = 10, text = "Today", variable=todaySelector, onvalue=1, offvalue=0)
todayButton.place(x=325, y=125)


#Create combobox to select results type
selectedType = StringVar()
textlblType = Label(window, text="*Choose results type:")
textlblType.place(x=75, y=175)
comboOptions = ['mixed', 'recent', 'popular']
combo = ttk.Combobox(window, values = comboOptions, textvariable=selectedType, width=22)
combo.place(x=250, y=175)


#Create number of tweets to pull
numTweets = StringVar()
searchNum = Entry(window, width=25, textvariable=numTweets)
searchNum.place(x=250, y=225)
textlblNum = Label(window, text="*Enter number of tweets to pull:")
textlblNum.place(x=75, y=225)


textlblvadertextblob = Label(window, text="Select which sentiment analyzer to use (or both):")
textlblvadertextblob.place(x=75, y=275)
#Variable to get the checkbox status, checked = 1, unchecked = 0
VADERselector = IntVar()
TextBlobselector = IntVar()
#Create check button for textblob/VADER selection
VADERbutton = Checkbutton(window, width = 15, text = "VADER", variable=VADERselector, onvalue=1, offvalue=0)
TextBlobbutton = Checkbutton(window, width = 15, text = "TextBlob", variable=TextBlobselector, onvalue=1, offvalue=0)
VADERbutton.place(x=75, y=300)
TextBlobbutton.place(x=250, y=300)


#Set output text
outputText = "Output will be displayed here."
outMsg = Message( window, text=outputText, font = 36, width = 400, relief=RAISED)
outMsg.place(x=450, y=75)


#Create Execute button
executeButton = Button(window, text="Execute", fg = "white", bg = "green", relief = "raised", height = 2, width = 10, command=output)
executeButton.place(x=75, y=350)

    
#Create Quit/Exit button
exitButton = Button(window, text="Quit", fg = "white", bg = "red", relief = "raised", height = 2, width = 10, command=exitProgram)
exitButton.place(x=275, y=350)


#Create print graph button
testerButton = Button(window, text="Create Graph", fg = "white", bg = "blue", relief = "raised", height = 2, width = 15, command=printGraph) #command=openTesterWindow)
testerButton.place(x=75, y=450)

#Create analyze news button
newsButton = Button(window, text="Analyze News", fg = "black", bg = "yellow", relief = "raised", height = 2, width = 15, command=analyzeNews)#command=printGraph) #command=openTesterWindow)
newsButton.place(x=275, y=450)

#Create help button
helpButton = Button(window, text="About", relief = "groove", height = 1, width = 8, command=launchHelp) #command=openTesterWindow)
helpButton.place(x=0, y=0)

'''
#Create combobox for crypto selection
selectedCrypto = StringVar()
textlblTypeCrypto = Label(window, text="Choose crypto:")
textlblTypeCrypto.place(x=106, y=525)
comboOptionsCrypto = ['bitcoin', 'dogecoin', 'cardano', 'litecoin',\
                      'crypto-com-coin', 'chia-network', 'scala']

#not working - eth, bin, xrp, teth, 
'''

comboCrypto = ttk.Combobox(window, values = comboOptionsCrypto, textvariable=selectedCrypto, width=15)
comboCrypto.place(x=206, y=525)


#Variable to get the checkbox status, checked = 1, unchecked = 0
Cryptoselector = IntVar()
#Create check button for textblob/VADER selection
Cryptobutton = Checkbutton(window, width = 1, variable=Cryptoselector, onvalue=1, offvalue=0)
Cryptobutton.place(x=75, y=525)

window.iconbitmap("img.ico")

#Create button to launch API enter window
apiButton = Button(window, text="Edit API Keys", relief = "groove", height = 1, width = 12, command=launchEditAPIWindow)
apiButton.place(x=75, y=0)



#Create the GUI
window.mainloop()
