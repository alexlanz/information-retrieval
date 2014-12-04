from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import time

remove = ('headers', 'footers')

newsgroups_train = fetch_20newsgroups(subset="train", remove=remove, data_home="./newsgroups/train")
newsgroups_test = fetch_20newsgroups(subset="test", remove=remove, data_home="./newsgroups/test")

Y_train = newsgroups_train.target
Y_test = newsgroups_test.target

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
X_train = vectorizer.fit_transform(newsgroups_train.data)
X_test = vectorizer.transform(newsgroups_test.data)


# The function used to time a training and classification on 3 examples
def time_trial(num_features, index, X_train, X_test, Y_train, Y_test):
    """Time Knn classifiers training time + classification of three instances.

    Keyword arguments:
    Sparse -- if False, the X_train, and X_test data will be densified
    num_features -- The number of features to slice the training data down to
    X_train -- Used as input to the classifier
    X_test -- Used as data for the classifier to predict on
    Y_train -- labels for X_train
    Y_test -- labels for X_test
    """
    # slice the data
    Y_train = Y_train[0:1000]
    X_train = X_train[0:1000, 0:num_features]
    X_test = X_test[:, 0:num_features]
 
    # Densify data, originally sparse
    X_train = X_train.toarray()
    X_test = X_test.toarray()
 
    # Initialize KNN
    neigh = KNeighborsClassifier(n_neighbors=3)
 
    # Begin Timing
    start = time.clock()
 
    # Train on data
    neigh.fit(X_train, Y_train)
 
    # Predict
    neigh.predict(X_test[index])
    return (time.clock() - start)

# random test examples to classify
index = np.random.randint(0, X_test.shape[0], size=(3, ))

# Plotting code starts here, use the following flag to enable/disable it
num_features = range(200, 20200, 1000)
 
dense_line = [time_trial(num_features[i], index, X_train, X_test, Y_train, Y_test) for i in range(20)]
plt.plot(num_features, dense_line, 'r', label="Dense Format")
plt.title("KNN")
plt.ylabel("""Elapsed Time (Seconds): KNN Training +
           Classifying Three Instances""")
plt.xlabel('Input Data Number of Features')
plt.savefig("knn.png")