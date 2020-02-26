from web_app.models import User
import numpy as np


user1 = User.query.filter(User.name == user1_name).one()
user2 = User.query.filter(User.name == user2_name).one()
user1_embeddings = np.array([tweet.user1_embedding
                             for tweet in user1.tweets])
user2_embeddings = np.array([tweet.user2_embedding
                             for tweet in user2.tweets])
embeddings = np.vstack([user1_embeddings, user2_embeddings])
labels = np.concatenate([np.ones(len(user_1_tweets)), np.zeroes(len(user_2_tweets))])
