from elasticsearch import Elasticsearch
from utils import Timer

es = Elasticsearch()

# Start timer
timer = Timer()
timer.start()

# Query
#result = es.search(index="document-index", body={"query": {"match_all": {}}})
result = es.search(
    index='document-index',
    doc_type='book',
    body={
      'query': {
        'filtered': {
          'query': {
            'match': {'text': 'fix'}
          }
        }
      }
    }
)

print("Got %d Hits:" % result['hits']['total'])

for hit in result['hits']['hits']:
    print(hit["_source"]["name"])
    #text = hit["_source"]["text"]
    #print(text.encode('utf-8'))

# Stop timer
timer.stop()
print("Search time: " + timer.getElapsedMillisecondsString())