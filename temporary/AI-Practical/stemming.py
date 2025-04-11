from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ["python", "pythonly", "phythoner", "pythonises"]

for w in example_words:
    print(ps.stem(w))

