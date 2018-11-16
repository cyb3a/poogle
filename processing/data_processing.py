# -*- coding: utf-8 -*-

import json
import nltk
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer  # Support for German language stemming

from processing.secrets import pwd, usr, hst, dab
import pymysql

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
with open(json_data) as raw:
    data = json.load(raw)

# Tokenize & Lowercase & Remove Stopwords
words = {}
for report in data:
    x = word_tokenize(report['Title']+' '+report['Content'])
    y = [tok.lower() for tok in x if tok.lower() not in stopwords]
    words[report['URL']] = y

# Look for collocations with WHATEVER.collocations() -> common phrases, 'Eigennamen'
# collocs = {}

# Stem
normed = {}

for url, tokens in words.items():
    normed[url] = [stemmer.stem(w) for w in tokens]

## Count Tokens TODO

# Database
pymysql.install_as_MySQLdb()
import MySQLdb
db = pymysql.connect(host=hst,
                       user=usr,
                       passwd=pwd,
                       db=dab)

try:
    cur = db.cursor()
    cur.executemany("""
        INSERT INTO reports (URL, Title, Locations, Dates, Content, CreatedAt)
        VALUES (%(URL)s, %(Title)s, %(Locations)s, %(Dates)s, %(Content)s, %(CreatedAt)s)""", data)
    db.commit()
finally:
    cur.close()

db.close()
