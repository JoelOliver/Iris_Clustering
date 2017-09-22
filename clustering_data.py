import numpy as np
from near_centroid import *
from centroid_mean import *

def load_data(filename):
    dataset = np.genfromtxt(filename, delimiter=' ',
                            dtype=float, usecols=(0, 1, 2, 3))

    np.random.shuffle(dataset)

    return dataset


def clustering(dataset, k):
    centroids = []
    for index in range(k):
        centroids.append([dataset[index + 1], index + 1])

    assignedClusters = assign_centroids(dataset,centroids)

    centralized = centroid_mean(centroids,assignedClusters,dataset)

    return centralized

clustering(load_data('iris.txt'), 3)
