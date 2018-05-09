import tweepy
import warnings
from afinn import Afinn
from tweepy import OAuthHandler
import json
import re
import couchdb
from tweepy.streaming import StreamListener


# putting data into database
database_name = 'twitter'
server = "http://115.146.86.96:5984"


# getting twitter customer and access keys
consumer_key = 'v0972w9aptiA8Dzm97sGFykPY'
consumer_secret = 'e9P4IMHyWEIwqwKiYVu4qDwXLMBooockFeqs5lwkjhCvJ0efle'
access_key = '988266868828815360-LUDs2XCggWF57JVCZpOSvDTyxYNxEcg'
access_secret = 'GdkzCMPkAFhJU6jHfr15ZD4TmSETTW41RQLxp3lNODoVL'


# OAuth
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    print("Authentication done")
except:
    print("Error: Authentication Failed")


# database connection error handling
try:
    couch = couchdb.Server(server)
    database = couch[database_name]
    print("DataBase Intialized")
except:
    print("Cannot find CouchDB Server ... Exiting\n")


# removing tweets with '@'
def clean_tweet(tweet):
    try:
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    except Exception as exc:
        print("cleaning failed")


# getting sentiment score for the cleaned tweets
def get_sentiment_score(tweet, lang):
    try:
        cleaned = clean_tweet(tweet)
        afinn = Afinn(language=lang)
        sentiment = afinn.score(cleaned)
        print(cleaned, " ", sentiment)
        return sentiment
    except Exception as ex:
        # print(tweet)
        warnings.warn("sentiment analysis failed")


# getting Twitter data and saving it in CouchDB using Stream Listeners
class StreamListener(tweepy.StreamListener):
      #print("In listner")

    def on_data(self, data):
        try:
            # converts to json format then saves in couchdb
            json_data = json.loads(data)
            if json_data["text"].startswith("RT ") and data.isRetweeted:
                pass
            else:
                tweet_lang = json_data["lang"]
                sentiment_score = get_sentiment_score(
                    json_data["text"], tweet_lang)
                if sentiment_score is None:
                    document = {"tweet_data": json_data,
                                "sentiment": 'No sentiment found'}
                else:
                    document = {"tweet_data": json_data,
                                "sentiment": sentiment_score}
                # saves the document to database
                database.save(document)
                #print('added: ', document)
            return True
        except Exception as ex:
            #print "fail"
            warnings.warn("Failure")


def call_stream():
    try:
        l = tweepy.streaming.Stream(auth, StreamListener())
        l.filter(locations=[110.95, -54.83, 159.29, -11.35])
    except Exception as ex:
        warnings.warn("Streaming failed")


call_stream()
