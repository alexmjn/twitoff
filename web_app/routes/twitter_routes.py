# pylint: disable=import-error
import basilica
from flask import Blueprint, render_template, jsonify
from web_app.twitter_service import twitter_api
from web_app.models import db, User, Tweet
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

twitter_api_client = twitter_api()

twitter_routes = Blueprint("twitter_routes", __name__)

# Print current users
# TODO: the Twitter users are loading into the database, but
# we're getting an "Oops- User not found!" message there.
@twitter_routes.route("/users")
@twitter_routes.route("/users.json")
def list_users():
    users=[]
    user_records = User.query.all()
    for user in user_records:
        print(user)
        d = user.__dict__
        del d["_sa_instance_state"]
        users.append(d)
    return jsonify(users)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)

    try:

        twitter_user = twitter_api_client.get_user(screen_name)

        # find or create database user:
        db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
        db_user.screen_name = twitter_user.screen_name
        db_user.name = twitter_user.name
        db_user.location = twitter_user.location
        db_user.followers_count = twitter_user.followers_count
        db.session.add(db_user)
        db.session.commit()

        #breakpoint()

        statuses = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=50, exclude_replies=True, include_rts=False)
        db_tweets = []
        for status in statuses:
            print(status.full_text)
            print("----")

            # Find or create database tweet:
            db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
            db_tweet.user_id = status.author.id # or db_user.id
            db_tweet.full_text = status.full_text

            with basilica.Connection(API_KEY) as c:
                embeddings = list(c.embed_sentence(sentences))
            embedding = basilica_client.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet

            db_tweet.embedding = embedding
            db.session.add(db_tweet)
            db_tweets.append(db_tweet)
        db.session.commit()

        return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets

    except:
        return jsonify({"message": "OOPS User Not Found!"})
