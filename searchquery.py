from elasticsearch import Elasticsearch

from query import *
# from rules import process

INDEX = 'sample2'
client = Elasticsearch(['http://localhost:9200'])

def process_query(query):
    # if any(word in query for word in top_words):
    #     print("Best search query")
    #     query_body = best_search(query)
    if '''”''' in query or '''"''' in query:
        print("Exact search query")
        query_body = exact_search(query)
    elif '*' in query:
        print("wild card search query")
        query_body = wild_card_search(query)
        print(query_body)
    elif '@' in query:
        print("multi match search query")
        query_body = multi_match(query)
        print(query_body)
    else:
        print("basic search query")
        query_body = basic_search(query)
    return query_body


def search(query):
    query_body = process_query(query)
    print('Searching...')
    resp = client.search(index=INDEX, body=query_body)
    return resp
