from elasticsearch import Elasticsearch
from documents import DocumentManager
from utils import Timer

es = Elasticsearch()

# Delete old index
#es.indices.delete(index='document-index')

# Start timer
timer = Timer()
timer.start()

# Create new index
documentManager = DocumentManager("documents")
documents = documentManager.loadDocuments()

for document in documents:

    text = documentManager.getDocumentText(document)

    doc = {
        'name': document.getPath(),
        'text': text
    }

    result = es.index(index="document-index", doc_type="book", body=doc)
    print("Document " + document.getPath() + " added to index: " + str(result["created"]))


# Refresh the index
es.indices.refresh(index="document-index")

# Stop timer
timer.stop()
print("Index creation time: " + timer.getElapsedMillisecondsString())