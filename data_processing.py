# -*- coding: utf-8 -*-

import json
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer  # Support for German language stemming

nltk.download('punkt')
stopWords = set(stopwords.words('german'))
stemmer = SnowballStemmer("german")

# Read the Json file
json_data = 'testing.json'  # change here
raw = open(json_data)
data = json.load(raw)

# Tokenize
words = []
for report in data:
    words.append((report['URL'], word_tokenize(report['Title']+" "+report['Content'])))

# Look for collocations with WHATEVER.collocations() -> common phrases, 'Eigennamen'
collocs = []

# Normalize & Stem
normed = []
for tokens in words:
    normed.append((tokens[0], [stemmer.stem(w.lower()) for w in tokens[1]]))  # lowercase

# Remove Stopwords & Punctuation

## Count Tokens