from elasticsearch import Elasticsearch
from utils import Timer

es = Elasticsearch()

queries = []

queries.append({
    'query': {
        'filtered': {
            'query': {
                'match': {'text': 'yogi'}
            }
        }
    }
})

queries.append({
    'query': {
        'bool': {
            'must': [
                { 'term': { 'text': 'yogi' } },
                { 'term': { 'text': 'atkinson' } }
            ]
        }
    }
})

queries.append({
    'query': {
        'bool': {
            'must': [
                {
                    'bool': {
                        'should': [
                            { 'term': { 'text': 'yogi' } },
                            { 'term': { 'text': 'atkinson' } },
                            { 'term': { 'text': 'gutenberg' } }
                        ]
                    }
                },
                {
                    'bool': {
                        'must': [
                            { 'term': { 'text': 'status' } }
                        ],
                        'must_not': [
                            { 'term': { 'text': 'code' } }
                        ]
                    }
                }
            ]
        }
    }
})

queries.append({
    'query': {
        'wildcard': {
            'text': {
                'value': 'in*ma*on'
            }
        }
    }
})


queries.append({
    'query': {
        'wildcard': {
            'text': {
                'value': 'hel*'
            }
        }
    }
})

queries.append({
    'query': {
        'wildcard': {
            'text': {
                'value': '*ogi'
            }
        }
    }
})



for query in queries:

    # Start timer
    timer = Timer()
    timer.start()

    # Query
    #result = es.search(index="document-index", body={"query": {"match_all": {}}})
    result = es.search(
        index='document-index',
        doc_type='book',
        body=query
    )

    # Stop timer
    timer.stop()

    # Result
    print("\nSearch time: " + timer.getElapsedMillisecondsString())
    print("Got %d Hits:" % result['hits']['total'])

    for hit in result['hits']['hits']:
        print(hit["_source"]["name"])
        #text = hit["_source"]["text"]
        #print(text.encode('utf-8'))