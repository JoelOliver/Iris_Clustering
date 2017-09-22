import numpy as np
from near_centroid import *


def load_data(filename):
    dataset = np.genfromtxt(filename, delimiter=' ',
                            dtype=float, usecols=(0, 1, 2, 3))

    np.random.shuffle(dataset)

    return dataset


def clustering(dataset, k):
    centroids = []
    for index in range(k):
        centroids.append([dataset[index + 1], index + 1])

    assignedClusters = np.array([], dtype=int)

    for data in dataset:
        minor_dist = dist_centroid(data, centroids[0][0])
        closest = centroids[0]
        for centroid in centroids:
            if(dist_centroid(data, centroid[0]) <= minor_dist):
                closest = centroid
        assignedClusters = np.append(assignedClusters, closest[1])

    return assignedClusters

print(clustering(load_data('iris.txt'), 3))
