# What is this?
This project is something I created trying to learn/experiment with creating graphical user interfaces (GUI) with python. I thought it would be interesting to create a program that would give a rough general sentiment of a topic for a given date and make it easy enough to use that almost no technical skill would be required.

# What does it do?
There are four main files included as part of this repository, `Gui.pyw`, `graph.pyw`, `nlp.pyw` and `config.ini`.

`Gui.pyw` - This is the main file as well as the one that should be executed to utilize the program. It creates the GUI and allows the user to enter all the required parameters to execute the program. Upon clicking the 'Execute' button the application will attempt to pull 100 tweets from the selected date using the provided keyword and spits out an average sentiment value which ranges from -1 to +1. Additionally, for ease a plan english description of the value is also printed, i.e. 'Good' or 'Bad'. [See How can I use it?](https://github.com/ehoop10/Twitter-Sentiment-Analyzer/blob/main/README.md#how-can-i-use-it) for more information on setting the parameters.

`graph.pyw` - The main GUI contains a button labeled 'Create Graph', after running the program with the needed parameters and once the results have been displayed you may click this button to create a bar graph which shows the number of tweets which fit into each defined sentiment category. See Sentiment categories for more information on this

`nlp.pyw` - This file contains the Natural Language Processing (NLP) component of this projects and is responsible for the actual sentiment analysis perfromed by using Vader Sentiment analysis.

`config.ini` - This is the file which stores Twitter API keys which are needed to use this application. See How can I use it? for more information

# How can I use it?
To use this project download/clone the repository and install the needed dependencies. Then execute the `Gui.pyw` file. (Note: if you are unaware .pyw simply means that the python console windows is not launched when the application is executed, unlike the standard .py extension.)

Upon executing `Gui.pyw` you will be met with the main window. The first thing you must do in order to use the application is to add you Twitter API keys using the 'Edit API Keys' button in the top left of the window. See 'How can I get Twitter API keys?' for instructions. Oce you have your API keys entered, save them to `config.ini` by clicking the 'Set keys' button. You should then recieve a pop-up stating 'API keys set in config.ini', not simply click the 'Quit' button and restart the program. Great! Now your ready to use it! Enter a search term you would like to analyze along with a date in format YYYY-MM-DD and finally choose what result type you would like to pull. See Result Types for more info on this. Then click 'Execute'. After a few seconds the text box on the right will populate with the ouput data. If you wish to see a breakdown of the data pulled click 'Create Graph'.

### Main window
![Main View](https://github.com/ehoop10/Twitter-Sentiment-Analyzer/blob/main/Twitter%20Analyzer/readmeImages/main.JPG)


### Edit API Keys
![Edit API Keys](https://github.com/ehoop10/Twitter-Sentiment-Analyzer/blob/main/Twitter%20Analyzer/readmeImages/setAPI.JPG)


### Edit API Keys pop-up
![pop-up](https://github.com/ehoop10/Twitter-Sentiment-Analyzer/blob/main/Twitter%20Analyzer/readmeImages/setAPIpopup.JPG)


### Example config.ini
![config](https://github.com/ehoop10/Twitter-Sentiment-Analyzer/blob/main/Twitter%20Analyzer/readmeImages/configINI.JPG)

### Example Create Graph
![Create Graph](https://github.com/ehoop10/Twitter-Sentiment-Analyzer/blob/main/Twitter%20Analyzer/readmeImages/createGraph.JPG)


# How can I get Twitter API keys?
To get twitter API keys see the Twitter documentatint for [How to get access to the Twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)


# Sentiment Categories
VADER Sentiment analysis scored the sentiment of a statement from -1 (most negative) to +1 (most positive), this program breaks this range down into 7 categories to make it easier to interpret. These categories are as follows:

| Numeric Score| Category|
|--------------|---------|
| -1.0 to -0.9| Very Bad|
| -0.9 to -0.3| Bad|
| -0.3 to -0.05| Slightly Bad|
| -0.05 to 0.05| Neutral|
| 0.05 to 0.3| Slightly Good|
| 0.3 to 0.9| Good|
| 0.9 to 1.0| Very Good|

# Result Types
| Type| Details|
|-----|--------|
| Mixed| Include both popular and real time results in the response.|
| Recent| Return only the most recent results in the response|
| Popular| return only the most popular results in the response|

# What is VADER?
VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. If you would like more information see the project [here](https://github.com/cjhutto/vaderSentiment).


# Donations
BTC - bc1q8wdfa8xvqhgdyudy9hdaqzelps2rarl9vzas4m <br/>
ETH - 0x77f533a7D98B6888f90543959fB5b8Ea3539eE0c <br/>
LTC - LSfCvorJ4FUUKZiKnw1f2xaH2akdUm44AS  <br/>
