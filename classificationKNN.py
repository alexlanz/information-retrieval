from session import Session
from sessionRepository import SessionRepository
from sklearn.neighbors import KNeighborsClassifier

session01 = Session(1, 120, 4, 2, True, True)
session02 = Session(2, 4030, 20, 16, False, False)
session03 = Session(3, 1325, 30, 10, False, False)
session04 = Session(4, 110, 5, 2, True, True)
session05 = Session(5, 1223, 50, 30, False, False)

repository = SessionRepository();
repository.add(session01);
repository.add(session02);
repository.add(session03);
repository.add(session04);
repository.add(session05);

X = repository.getAllVectors()
y = repository.getAllBuyingLabels()

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

sessionPredict = Session(6, 117, 3, 1, True, False)
predictData = [sessionPredict.getVector()]
predictions = neigh.predict(predictData)

print(predictions)