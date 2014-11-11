from index import Index
from parser import IndexParser
from parser import QueryParser
from query import QueryExecutor
from statistics import Statistic

# Parser
indexParser = IndexParser()

# Index
index = Index(indexParser)
print("Time for creating the index: " + index.getTimer().getElapsedMillisecondsString() + "\n")

# Query
print("Query execution:")
print("You can leave the program by entering 'exit'.\n")

queryParser = QueryParser(index.getNGrams())
queryExecutor = QueryExecutor(index)
statistics = Statistic()

while True:
    query = input("Query: ")

    if query == "exit":
        break

    # Query execution
    parsedQuery = queryParser.parse(query)

    '''for query in parsedQuery:
        print('Search Tokens')
        for token in query.getSearchTokens():
            print(token)

        print('Excluded Tokens')
        for token in query.getExcludedTokens():
            print(token)'''

    result = queryExecutor.executeQuery(parsedQuery)

    print("Rank\tSimilarity\tDocument")

    position = 1
    for item in result:
        print("" + str(position) + "\t" + "{0:.3f}".format(item.getRank()) + "\t" + item.getDocument().getPath())
        position += 1

    print("Parse time: " + queryParser.getTimer().getElapsedMillisecondsString())
    print("Execution time: " + queryExecutor.getTimer().getElapsedMillisecondsString())
    print("Number of results: " + str(len(result)) + "\n")

    recallList = statistics.getRecallAtk(result)
    precisionList = statistics.getPrecisionAtk(result)

    statistics.printRecall(recallList)
    statistics.printPrecision(precisionList)
    print("")

print("Exiting form query execution ...\n")
