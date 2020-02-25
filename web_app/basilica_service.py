import basilica
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("BASILICA_API_KEY")
sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]
with basilica.Connection(API_KEY) as c:
    embeddings = list(c.embed_sentences(sentences))
print(embeddings)
[[0.8556405305862427, ...], ...]
