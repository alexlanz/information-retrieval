from index import Index
from index import IndexSource
from parser import Parser
from parser import ParserType
from query import QueryExecutor

# Index source
print("Do you want to create a new index or load an stored index?")
print("[1] Create new index")
print("[2] Load stored index")

while True:
    indexOption = input("What's your choice [1/2]: ")

    if indexOption == '1':
        indexSource = IndexSource.new
        break
    elif indexOption == '2':
        indexSource = IndexSource.stored
        break

    print("Invalid option '" + indexOption + "', please choose again.")


# Parser
parser = Parser(ParserType.simple)

# Index
index = Index(indexSource, parser)
print("Time for creating the index: " + index.getTimer().getElapsedMillisecondsString() + "\n")

# Query
print("Query execution:")
print("You can leave the program by entering 'exit'.\n")

queryExecutor = QueryExecutor(index)

while True:
    query = input("Query: ")

    if query == "exit":
        break

    # Query execution
    parsedQuery = parser.parseQuery(query)
    result = queryExecutor.executeQuery(parsedQuery)

    print("Number\tRank\tDocument")

    position = 1
    for item in result:
        print("" + str(position) + "\t" + "{0:.3f}".format(item.getRank()) + "\t" + item.getDocument().getPath())
        position += 1

    print("Execution time: " + queryExecutor.getTimer().getElapsedMillisecondsString())
    print("Number of results: " + str(len(result)) + "\n")

print("Exiting form query execution ...\n")


# Store index
print("Do you want to store the index?")
while True:
    indexOption = input("[y/n]: ")

    if indexOption == 'y':
        index.storeIndex()

        timerForIndexStoring = index.getTimer()
        print("Time for storing the index: " + timerForIndexStoring.getElapsedMillisecondsString() + "\n")

        break
    elif indexOption == 'n':
        break

    print("Invalid option '" + indexOption + "', please choose again.")
