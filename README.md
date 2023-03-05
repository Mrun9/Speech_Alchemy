Speech Alchemy
CCOEW
Pune, 411052

*Currency Exchange Rate Prediction*

This model predicts the approximate Dollar to INR conversion rate at a given particular day on the basis of training data for the last 2.5 years and testing data of the last 6 months of the year 2022.



Models


1. USD to INR value prediction: We have made use of Decision Tree Regressor for
predicting the values of USD over a period of 2 years - starting from 1st Jan ‘20 and
ending 31st Dec ‘25. We have extracted the data for training of 2.5 years and have tested
for 6 months with an accuracy of 65%. Here for training we have made use of ‘Day Count’
that refers to ‘Dates’ as an independent variable (1/1/20 refers to ‘0’th day, 2/1/20 refers
to ‘1’ st day, ... ) and the ‘Price’ of USD in INR as a dependent variable.


2. Sentiment Analysis: Here we extracted 2000 tweets containing the keyword INR currency
exchange rate. Columns of our final data frame include text, subjectivity, polarity, analysis of
polarity in words, and sentiment score. Column text represents tweets after tweets are
preprocessed and unwanted characters are removed. Subjectivity refers to the degree to
which a person is personally involved in an object. Polarity refers to the strength of an
opinion. It could be positive or negative. We then give sentiment_score as dependent
variable and 1 USD= as independent variable to the linear regression model and plot the
graph to show roughly the correlation between usd-inr exchange rates and sentiment of
tweets .


Deployment Specifications

We have made use of Streamlit module in python to deploy our website
1. Type this in vscode terminal : streamlit run ./app.py
2. To obtain the sentiment analysis :
● Pip install streamlit in the Google Colab
● Pip install pyngrok in the next cell
● Streamlit run SentimentAnalysis.py &amp; npx localtunnel –port 8501

Github repository : https://github.com/Mrun9/Speech_Alchemy


Modules used in project:

1. Snscrape- Python library which does not require an API and
2. SentimentIntensityAnalyzer
3. LinearRegression - to find correlation between sentiments of tweets and exchange
rate
4. Word_tokenize
5. NLTK - for classifying sentiment into positive, negative or neutral
6. DecisionForestRegressor - for prediction of Prices of USD
7. Streamlit - for frontend
