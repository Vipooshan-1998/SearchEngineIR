import json
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Read JSON file
with open('corpus/corpusjson.json', 'r', encoding='utf-8') as json_file:
    json_array = json.load(json_file)

# Index documents in Elasticsearch
for doc in json_array:
    res = es.index(index='sample2', document=doc)
    print(res)