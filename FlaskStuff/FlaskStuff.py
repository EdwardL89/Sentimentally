import tweepy

#TextBlob is a Python Natural Language Processing Library
from textblob import TextBlob
from flask import Flask, render_template, request

app = Flask(__name__);

@app.route('/')
def index():
    return 'This is the home page'
 

@app.route('/profile/', methods=['POST'])
def profile():
    text = request.form['@twitter']
    consumer_key = 'TCNvmZhcLVgG66ktybasO6ZZQ'
    consumer_secret = '4n1AaDp8oSWMxJLaSz35WBlLuLgsyF7Xu8RYbfJAOkfBSy2UQF'
    access_token = '2607970348-zbW69Qxp55mHpd6oCacTulkN3QRuAONo1qSXbLI'
    access_token_secret = 'A6q3cgql3JQOdS05mDbOReuZ9EF3Q6ztbHRJAFGfMHy4v'

    #Tweepy API methods to fetch tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #Holds the text from the home page that the user entered
    stringtobesearched = text

    #Tweepy API method to search the string
    public_tweets = api.search(stringtobesearched)

    #Polarity and Subjectivity on input
    polarityans = 0
    subjectivityans = 0
    count = 0
    tweetCounter = 0;
    sentiCounter = 0;
    #Our first version will statically allocate space for 6 tweets using the lists below
    tweetList = ['', '', '', '', '', '']
    sentimentList = ['', '', '', '', '', '']
    for tweet in public_tweets:
        #Insert the tweet's text into the tweetList.
        tweetList.insert(tweetCounter, tweet.text)
        analysis = TextBlob(tweet.text)
        if (analysis.sentiment.subjectivity != 0 and analysis.sentiment.polarity != 0):
            subjectivityans += analysis.sentiment.subjectivity
            polarityans += analysis.sentiment.polarity
            count += 1
            #Insert the sentiment analysis in the sentimentList
            sentimentList.insert(sentiCounter, analysis.sentiment)
            sentiCounter += 1
        tweetCounter += 1
    #calculate the average of the polarity scores. This value is what will be graphed in the bar graph at the bottom of the webpage.
    average1 = polarityans/count
    
    #return the values in the list to be displayed in HTML files
    return render_template("profile.html", value=tweetList[0], value2=tweetList[1], value3=tweetList[2], value4=tweetList[3], value5=tweetList[4], value6=tweetList[5], senti=sentimentList[0], senti2=sentimentList[1], senti3=sentimentList[2], senti4=sentimentList[3], senti5=sentimentList[4], senti6=sentimentList[5], average=average1)
     

@app.route('/profile/')
def profile1():
    #Twitter API keys and tokens to be used for Tweepy API
    consumer_key = 'TCNvmZhcLVgG66ktybasO6ZZQ'
    consumer_secret = '4n1AaDp8oSWMxJLaSz35WBlLuLgsyF7Xu8RYbfJAOkfBSy2UQF'
    access_token = '2607970348-zbW69Qxp55mHpd6oCacTulkN3QRuAONo1qSXbLI'
    access_token_secret = 'A6q3cgql3JQOdS05mDbOReuZ9EF3Q6ztbHRJAFGfMHy4v'

    #Tweepy API methods to fetch tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #This holds the string that user wants to search. However, I problem we encountered is upon launch, the
    #site crashes when the test is empty. To temporarily fix this, we placed a random string into the variable.
    stringtobesearched = "NBA"

    #Tweepy API method to search the string
    public_tweets = api.search(stringtobesearched)

    #The code below is the same as above in the profile() function.
    polarityans = 0
    subjectivityans = 0
    count = 0
    tweetCounter = 0;
    sentiCounter = 0;
    tweetList = ['', '', '', '', '', '']
    sentimentList = ['', '', '', '', '', '']
    for tweet in public_tweets:
        tweetList.insert(tweetCounter, tweet.text)
        analysis = TextBlob(tweet.text)
        if (analysis.sentiment.subjectivity != 0 and analysis.sentiment.polarity != 0):
            subjectivityans += analysis.sentiment.subjectivity
            polarityans += analysis.sentiment.polarity
            count += 1
            sentimentList.insert(sentiCounter, analysis.sentiment)
            sentiCounter += 1
        tweetCounter += 1
    
    average1 = polarityans/count
    
    return render_template("profile.html", value=tweetList[0], value2=tweetList[1], value3=tweetList[2], value4=tweetList[3], value5=tweetList[4], value6=tweetList[5], senti=sentimentList[0], senti2=sentimentList[1], senti3=sentimentList[2], senti4=sentimentList[3], senti5=sentimentList[4], senti6=sentimentList[5], average=average1)

if __name__ == "__main__":
    app.run(debug=True);
  
