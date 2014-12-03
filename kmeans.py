from __future__ import print_function
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.cluster import KMeans
from time import time

print("Loading 20 newsgroups dataset:")
dataset = fetch_20newsgroups(subset='train')

print("%d documents" % len(dataset.data))
print("%d categories" % len(dataset.target_names))
print()

labels = dataset.target
n_clusters = [5, 10, 15, 20]

print("Extracting features from the training dataset using TF-IDF:")
t0 = time()
vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english', use_idf=True)
X = vectorizer.fit_transform(dataset.data)

print("Time: %fs" % (time() - t0))
print("n_samples: %d, n_features: %d" % X.shape)
print()


# Calculate clustering

for k in n_clusters:
    print("Clustering with %d clusters" % k)
    print("---------------------------")
    km = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)

    t0 = time()
    km.fit(X)
    print("Time: %0.3fs" % (time() - t0))
    print()

    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))
    print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))
    print("Adjusted Rand-Index: %.3f" % metrics.adjusted_rand_score(labels, km.labels_))
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels, sample_size=1000))

    print()

    print("Top terms per cluster:")
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(k):
        print("Cluster %d:" % i, end='')
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
        print()

    print()
    print()
