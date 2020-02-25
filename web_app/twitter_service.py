import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def twitter_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

if __name__ == "__main__":
    api = tweepy.API(auth)
    user = api.get_user("Chrisalbon")
    #print("user", user)
    # User object has a lot of stuff!
    print(user.screen_name)
    print(user.followers_count)
    # breakpoint()
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)
