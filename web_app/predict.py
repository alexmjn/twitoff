from web_app.models import User
import numpy as np
from sklearn.linear_model import LogisticRegression
from flask import Blueprint, jsonify, request, render_template, flash

from web_app.models import User, Tweet, db
from web_app.basilica_service import connection as basilica_api_client

def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print("FETCHING TWEETS FROM THE DATABASE...")
    #can seed users if not in there
    # or can check to see if in there, pass an error
    # or can set up app to take any text input, then populate database
    # with tweets, then run.
    # can also wrap in a try block. try users, if not get users and
    # then provide things.
    # if screen_name_a in db.user.screen_name and screen_name_b in db.users.screen_name:
    #     pass
    # elif screen_name_a in db.users.screen_name:
    #     #add user b to users
    #     pass
    # elif screen_name_b in db.users.screen_name:
    #     #add user a to users
    #     pass
    # else:
    #     pass
    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()
    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets

    print("TRAINING THE MODEL...")
    embeddings = []
    labels = []
    for tweet in user_a_tweets:
        labels.append(user_a.screen_name)
        embeddings.append(tweet.embedding)

    for tweet in user_b_tweets:
        labels.append(user_b.screen_name)
        embeddings.append(tweet.embedding)

    classifier = LogisticRegression()
    classifier.fit(embeddings, labels)

    print("MAKING A PREDICTION...")
    #result_a = classifier.predict([user_a_tweets[0].embedding])
    #result_b = classifier.predict([user_b_tweets[0].embedding])

    example_embedding = basilica_api_client.embed_sentence(tweet_text)
    result = classifier.predict([example_embedding])

    return render_template("results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely= result[0]
    )
