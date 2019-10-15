import tweepy
import time
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)
# followback followers


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == "name":
        follower.follow()
        print(follower.name)
        break
# fav tweet based on tweet
search = 'python'
numbersoftweet = 2

for tweet in tweepy.Cursor(api.search, search).items(numbersoftweet):
    try:
        tweet.favorite()
        tweet.retweet()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
