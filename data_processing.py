# -*- coding: utf-8 -*-

import json
import nltk
from nltk import word_tokenize

nltk.download('punkt')

# Read the Json file
json_data = 'testing.json'  # change here
raw = open(json_data)
data = json.load(raw)

# Tokenize
words = []
for report in data:
    words.append((report['URL'], word_tokenize(report['Title']+report['Content'])))

## Remove Stopwords

## Count Tokens