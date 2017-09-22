import numpy as np
from near_centroid import *
def centroid_mean(centroids,assigned,dataset):
    # add idx and enumerate
    for idx,centroid in enumerate(centroids):
        indices = np.where( assigned == centroid[1])
        #print(indices)
        mean = 0;

        for index in indices[0]:
            mean = mean + dataset[index]

        centroids[idx][0] = (1/len(indices[0])) * mean

    return centroids


def assign_centroids(dataset,centroids):
    assignedClusters = np.array([], dtype=int)
    for data in dataset:
        minor_dist = dist_centroid(data, centroids[0][0])
        closest = centroids[0]
        for centroid in centroids:
            if(dist_centroid(data, centroid[0]) <= minor_dist):
                closest = centroid
        assignedClusters = np.append(assignedClusters, closest[1])

    return assignedClusters
