def sentiment_data():
    import tweepy
    from textblob import TextBlob
    import pandas as pd
    import numpy as np
    import re
    import os
    

    consumerKey = os.getenv("consumerKey")
    consumerSecret = os.getenv("consumerSecret")
    accessToken = os.getenv("accessToken")
    accessTokenSecret = os.getenv("accessTokenSecret")

    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

    authenticate.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(authenticate, wait_on_rate_limit = True)

    posts = api.user_timeline(screen_name = "Bloomberg", count = 1000, lang = "en", tweet_mode = "extended")

    df = pd.DataFrame([tweet.full_text for tweet in posts], columns=["Tweets"])

    def cleanTxt(text):
        text = re.sub(r"@[A-Za-z0-9]+", "", text)  #remove mentions
        text = re.sub(r"#", "", text)   #remove "#" synmbol
        text = re.sub(r"RT[\s]+", "", text)    # remove RT
        text = re.sub(r"https?:\/\/\S+", "", text) #remove hyperlink

        return text

    df["Tweets"] = df["Tweets"].apply(cleanTxt)

    list_of_impt_words = ["energy", "s&p 500", "technology", "5g", "retail", "oil", "electricity", "health", "real estate", "bank", "banks", "insurance", "tourist", "tourism", "car", "automobile", "investors"]
    df["Tweets"] = df["Tweets"].str.lower() 
    df = df[df["Tweets"].str.contains('|'.join(list_of_impt_words))]

    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity

    def getPolarity(text):
        return TextBlob(text).sentiment.polarity

    df["Subjectivity"] = df["Tweets"].apply(getSubjectivity)
    df["Polarity"] = df["Tweets"].apply(getPolarity)


    def getAnalysis(score):
        if score < 0:
            return "Negative"
        elif score == 0:
            return "Netural"
        else:
            return "Positive"

    df["Analysis"] = df["Polarity"].apply(getAnalysis)

    return df