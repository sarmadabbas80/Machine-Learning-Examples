import tweepy
from textblob import TextBlob

consumer_key = 'mba5W3n1iJ3K2kFw44aV7cLHi'
consumer_secret = 'QeRcuB2xabQpFVPMQEinCMKVfIOuzAU1hQkgBdDwW1J23bzyWV'

access_token = '272531257-MPf9Ag88Zmlih2c4454h8XpgzR7HTQMELQe0UL4o'
access_token_secret = 'ZDQ4xOFLMfiKFqk697amgLSp81YW5U2fFv9JUak6lXf8Q'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#TrumpRussia')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
