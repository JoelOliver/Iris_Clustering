import numpy as np

def centroid_mean(centroids,assigned,dataset):
    # add idx and enumerate
    for centroid in centroids:
        indices = np.where( assigned = centroid[1])
        mean = 0;
        for index in indices:
            mean = mean + assigned[index]
