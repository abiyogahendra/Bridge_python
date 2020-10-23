from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import config
from ANN import classify 
from controller import historyDetection
from helper import removeEmoji

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
            listener = StdOutListener(fetched_tweets_filename)
            auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
            auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
            stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
            stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:

            jsonData = json.loads(data)
            tweetNoEmoji = removeEmoji(jsonData["text"])
            #print(jsonData["text"])
            #print("=====================================================================")
            print("username : ", jsonData["user"]["screen_name"])

            classifyT = classify(tweetNoEmoji)
            classN = str(classifyT[0][0])
            classification = str(classifyT[0][1])
            
            print("=====================================================================")

            historyDetection(jsonData["user"]["screen_name"], tweetNoEmoji, classN, classification)
            #insert("negative", tweetNoEmoji)
            ##with open(self.fetched_tweets_filename, 'a') as tf:[]
            ##    tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
