# -*- coding: utf-8 -*-

import json
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer  # Support for German language stemming

nltk.download('punkt')
stemmer = SnowballStemmer("german")

# Read stopword file
# Source and more Information: https://solariz.de/de/downloads/6/german-enhanced-stopwords.htm
# punctuation added manually
stopwords_path = 'processing/german_stopwords_plain.txt'
with open(stopwords_path) as f:
    stopwords = [line.rstrip('\n') for line in f]

# Read the Json file
json_data = 'processing/testing.json'  # change here
raw = open(json_data)
data = json.load(raw)

# Tokenize & Lowercase & Remove Stopwords
words = []
for report in data:
    x = word_tokenize(report['Title']+' '+report['Content'])
    y = [tok.lower() for tok in x if tok.lower() not in stopwords]
    words.append((report['URL'], y))

# Look for collocations with WHATEVER.collocations() -> common phrases, 'Eigennamen'
collocs = []

# Stem
normed = []

for tokens in words:
    normed.append((tokens[0], [stemmer.stem(w) for w in tokens[1]]))  # lowercase

# Remove Stopwords & Punctuation
print(normed)
## Count Tokens