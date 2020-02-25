# pylint: disable=import-error

import basilica
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")


connection = basilica.Connection(API_KEY)

if __name__ == "__main__":

    sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all..."]

    with basilica.Connection(API_KEY) as c:
        embeddings = list(c.embed_sentences(sentences))
    print(embeddings)
    [[0.8556405305862427, ...], ...]
    # embedding - data type "generator" - need to convert.
    # embeddings - list.

    for embedding in embeddings:
        print(len(embedding))
        print(list(embedding))
        print("-------")
