# converting the json/dict file to csv

import pandas as pd
import json
import csv

json_file = open('D:/webcorpora/corpus.json', 'r')

dict = json.load(json_file)

json_file.close()

df = pd.DataFrame.from_dict(dict, orient='index')

df.rename_axis('Word').reset_index().assign(length = df.index.str.len())\
    .rename(columns={0:'Count'})

df.to_csv('D:/webcorpora/corpus.csv')
