import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np


def random_sample(low, high):
    return low + (high - low) * random.random()


def initialize_centroids(data, k):
    min_val = float('inf')
    max_val = float('-inf')

    for point in data:
        min_val = min(point, min_val)
        max_val = max(point, max_val)

    centroids = []
    for i in range(k):
        centroids.append(random_sample(min_val, max_val))

    return centroids


def get_distance(point_1, point_2):
    return ((point_1 - point_2)**2)**0.5


def get_labels(data, centroids):
    labels = []
    for point in data:
        min_dist = float('inf')
        label = None
        for i, centroid in enumerate(centroids):
            new_dist = get_distance(point, centroid)
            if min_dist > new_dist:
                min_dist = new_dist
                label = i
        labels.append(label)
    return labels


def update_centroids(points, labels, k):
    new_centroids = [0 for i in range(k)]
    counts = [0] * k

    for point, label in zip(points, labels):
        new_centroids[label] += point
        counts[label] += 1
    try:
        for i, x in enumerate(new_centroids):
            new_centroids[i] = x/counts[i]
    except:
        pass
    return new_centroids


def should_stop(old_centroids, new_centroids, threshold=0):
    flag = False
    total_movement = 0
    for old_point, new_point in zip(old_centroids, new_centroids):
        if get_distance(old_point, new_point) <= threshold:
            flag = True
    return flag


def main(data, k):

    centroids = initialize_centroids(data, k)
    print(centroids)
    while True:
        old_centroids = centroids
        labels = get_labels(data, centroids)
        print(labels)
        centroids = update_centroids(data, labels, k)
        print(centroids)
        if should_stop(old_centroids, centroids):
            break

    print("final labels: ", labels)
    print("final centroids: ", centroids)
    centroids = np.array(centroids)

    plt.scatter(data, np.zeros_like(data) + 2, c=labels, cmap='viridis')
    plt.scatter(centroids, np.zeros_like(centroids) + 2, s=100, c='red')
    plt.show()


values = pd.read_csv("gre.csv")
dataset = values['GRE Score'].to_numpy()

main(dataset, 2)
