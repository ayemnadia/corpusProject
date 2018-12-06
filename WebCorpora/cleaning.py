import json
import re

# the scraped file by Scrapy
file_news = '/repository/newsCrawler/newsCrawler/spiders/kompas_edu.json'

# this file will be created automatically when cleaning process is done
# and containing the collected 'desc' item
file_clean = '/repository/kompas_edu_clean.txt'

# this file is containing the list of words that appear and counting them
corpus_freq = '/repository/corpus.json'

with open(file_news) as data:
    data = json.load(data)

with open(file_clean, 'w') as data2:
    for i in data:
        json.dump(i['desc'], data2)

file = open(file_clean, 'rt')
text = file.read()
file.close()

words = re.sub('[^\x00-\x7F]+', '', text) # Non-ASCII character removal
words = re.sub('\W+', ' ', words) # Symbol removal
words = re.sub('\d+', ' ', words) # Numeric removal
words = re.sub(' +',' ', words) # Space Replacing
words = words.lower() # Case Folding

with open(file_clean, 'w') as out:
    out.write(words)

# create file json
with open(file_clean, 'r') as input, open(corpus_freq, 'r') as out:
    words = input.read().split()
    corpus = json.load(out)

    for word in words:
        if word not in corpus:
            corpus[word] = 1
        else:
            corpus[word] += 1

with open(corpus_freq, 'w') as f:
    json.dump(corpus, f, indent=2)
