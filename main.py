from index import IndexSource
from index import Index
from utils import Timer
from output import Output

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


# Index
index = Index(indexSource)

timerForIndexCreation = index.getTimer()
print("Time for creating the index: " + timerForIndexCreation.getElapsedMillisecondsString() + "\n")


# Query
print("Query execution:")
print("You can leave the program by entering 'exit'.\n")

while True:
    query = input("Query: ")

    if query == "exit":
        break

    timer = Timer()
    timer.start()

    # Execution of the query

    timer.stop()
    print("Execution time: " + timer.getElapsedMillisecondsString() + "\n")

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