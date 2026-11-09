from textblob import TextBlob
# import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('brown')
# nltk.download('conll2000')
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('movie_reviews')
# nltk.download('wordnet')
# nltk.download('stopwords')
# exit(0)

text = 'How do I access a module written in Python from C?  You can get a pointer to the module object as follows:'

blob = TextBlob(text)

print(blob)

print(blob.sentences)
print(blob.words)
print(blob.tags)
print(blob.noun_phrases)
print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)
