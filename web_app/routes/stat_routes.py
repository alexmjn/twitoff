
from flask import Blueprint, jsonify, request, render_template, flash

#request lets us get stuff from the html form along with methods
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from web_app.models import User, Tweet, db
from web_app.basilica_service import connection as basilica_api_client
import numpy as np

stat_routes = Blueprint("stat_routes", __name__)

@stat_routes.route('/iris')
def iris():
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)

    return str(clf.predict(X[:2, :]))

@stat_routes.route("/predict", methods=["POST"])
def predict():
    print("predicting...")
    print("FORM DATA:", dict(request.form))
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]
    #can seed users if not in there
    # or can check to see if in there, pass an error
    # or can set up app to take any text input, then populate database
    # with tweets, then run.
    # can also wrap in a try block. try users, if not get users and
    # then provide things.
    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()
    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets
    #user_a_embeddings = [tweet.embedding for tweet in user_a_tweets]
    #user_b_embeddings = [tweet.embedding for tweet in user_b_tweets]
    embeddings = []
    labels = []
    for tweet in user_a_tweets:
        labels.append(user_a.screen_name)
        embeddings.append(tweet.embedding)

    for tweet in user_b_tweets:
        labels.append(user_b.screen_name)
        embeddings.append(tweet.embedding)
#test model by checking if we get accurate predictions on test data.
# this is a good test for you can you do this

    classifier = LogisticRegression()
    classifier.fit(embeddings, labels)
    # result_a = classifier.predict([tweets_a[0].embedding])
    # result_b = classifier.predict([tweets_b[0].embedding])



    test_embedding = basilica_api_client.embed_sentence(tweet_text)
    result = classifier.predict(test_embedding)
    breakpoint()
    return render_template("results.html",
    screen_name_a=screen_name_a,
    screen_name_b=screen_name_b,
    tweet_text=tweet_text,
    result=result)
