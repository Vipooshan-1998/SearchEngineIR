def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return q


def search_with_field(query, field):
    q = {
        "query": {
            "match": {
                field: query
            }
        }
    }
    return q


def multi_match(query, fields=['பாடல்', 'பாடல்வரிகள்'], operator='or'):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields"
            }
        }
    }
    return q


def wild_card_search(query):
    q = {
        "query": {
            "wildcard" : {
                "பாடல்வரிகள்": {
                    "value": query
                }
            }
        },
    }
    return q


def exact_search(query):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "type": "phrase"
            }
        }
    }
    return q
