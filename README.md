# What is this?
This project is something I created trying to learn/experiment with creating graphical user interfaces (GUI) with python. I thought it would be interesting to create a program that would give a rough general sentiment of a topic for a given date and make it easy enough to use that almost no technical skill would be required.

# What does it do?
There are four main files included as part of this repository, `Gui.pyw`, `graph.pyw`, `nlp.pyw` and `config.ini`.

`Gui.pyw` - This is the main file as well as the one that should be executed to utilize the program. It creates the GUI and allows the user to enter all the required parameters to execute the program. Upon clicking the 'Execute' button the application will attempt to pull 100 tweets from the selected date using the provided keyword and spits out an average sentiment value which ranges from -1 to +1. Additionally, for ease a plan english description of the value is also printed, i.e. 'Good' or 'Bad'. See Usage for more information on setting the parameters.

`graph.pyw` - The main GUI contains a button labeled 'Create Graph', after running the program with the needed parameters and once the results have been displayed you may click this button to create a bar graph which shows the number of tweets which fit into each defined sentiment category. See Sentiment categories for more information on this

`nlp.pyw` - This file contains the Natural Language Processing (NLP) component of this projects and is responsible for the actual sentiment analysis perfromed by using Vader Sentiment analysis.

`config.ini` - This is the file which stores Twitter API keys which are needed to use this application. See How can I use it? for more information

# How can I use it?
To use this project download/clone the repository and install the needed dependencies. Then execute the `Gui.pyw` file. (Note: if you are unaware .pyw simply means that the python console windows is not launched when the application is executed, unlike the standard .py extension.)


![Main View](https://github.com/ehoop10/Twitter-Sentiment-Analyzer/blob/main/Twitter%20Analyzer/readmeImages/main.JPG)




If you wish to collect your own data you may modify and use `gatedata.py`. Otherwise, this project comes with a sample file `output.csv` containing 14220 entries collected from June 27, 2021 23:02:21 GMT to July 03, 2021 03:11:18 GMT. These data were collected in 30 second intervals and shifted such that the last column displays the last price of SHIB 30 seconds in the future from the rest of that respective row. Note that if you decide to collect your own data you will need to perform this shift on the final column up to match with the time interval you are trying to model for.

Once you have your data collected and formatted you may execute `SHIB-ML-Gate.io.py` which allows you to select the input csv file. Once selected the script will ask for the number of prediction loops you would like to execute. A prediction loop is one iteration of the prediction cycle in which the script uses the trained model to predict the future price, waits for the timespan which it predicted for, pulls the actual price, compares this price to the predictions, and prints percent inaccuracy values for each of the 4 models. Additionally, a total average is kept such that if the predicition loop is run 10 times the average inaccuracies over the course of all 10 loops for each model are calculated and printed. This total average will print every ten loops if the number of loops selected is greater than 10.



# Data
For each of the three cryptocurrencies used the following data is collected

|Data | Currency pair| Time (given as UNIX epoch)| Base volume| Change percentage| High 24h| Highest bid| Low 24h| Lowest ask| Quote volume| last|
|-----|--------------|---------------------------|------------|------------------|---------|------------|--------|-----------|-------------|-----|
|Details| The pair of currency used(ex BTC-USD)|  The UNIX time of when the data was gotten| The amount traded in the past 24 hours given in the base currency (eg BTC)| The live percent change in the currency| The 24 high price| The current highest bid on the currency| The 24 hour low price| The current lowest ask price| The base volume equivalent for the other part of the pair (eg USD)| The last actual price the currency was traded at|


# Models (details taken from scikit-learn.org)
|Model | Full name| Details| Link to documentation|
|------|----------|--------|----------------------|
|SGD | Stochastic Gradient Descent| Linear model fitted by minimizing a regularized empirical loss with SGD| [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html)|
|GBR | Gradient Boosting Regressor| Gradient Boosting for regression | [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)|
|LR | Linear Regression| Ordinary least squares Linear Regression | [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)|
|RF | Random Forest Regressor | A random forest regressor | [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)|


# FAQ
### Why SHIB?
There isn't really a satisfying answer for this. I wanted to use a currency which had a relatively high volume/active trading, a fair bit of volatility, and was inexpensive. Do not take this project as an endorsement or support of the SHIB cryptocurrency as I do not feel strongly about it one way or another.

### Why 30 second intervals?
I wanted to be able to gather a fair bit of data without having to leave it running for a long time. Additionally, with the data at 30 second intervals it is easy to shift the last column and change the `time.sleep(30)` line in `SHIB-ML-Gate.io.py` to make the timescale longer while retaining a majority of the previously collected data. See [How can I use it?](https://github.com/ehoop10/SKlearn-Crypto-prediction/blob/main/README.md#how-can-i-use-it) for a little for information on this.



# Requirements
This script was written using Python v3.9.5 as well as gate_api, numpy, and sklearn which all may be install via PIP or by using the included requirements.txt (pip install -r requirements.txt)
You **DO NOT** need to have a current/valid Gate.io account to use this script as the API functions called do not require API keys to work.

# Disclaimer
The information provided by/with this project is for educational, informational, and entertainment purposes only and is not intended to be financial advice. You should not make any decision on investing/trading or otherwise based on the information provided by this project and understand that you are using any and all information available through this project as your own risk.

# Donations
BTC - bc1q8wdfa8xvqhgdyudy9hdaqzelps2rarl9vzas4m <br/>
ETH - 0x77f533a7D98B6888f90543959fB5b8Ea3539eE0c <br/>
LTC - LSfCvorJ4FUUKZiKnw1f2xaH2akdUm44AS  <br/>
SHIB (of course)- 0x8126B2E305f46C202cFecD04b673A960142AC26B
