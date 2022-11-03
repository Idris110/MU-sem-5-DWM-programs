import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np


def random_sample(low, high):
    return low + (high - low) * random.random()


def initialize_centroids(data, k):
    x_min = y_min = float('inf')
    x_max = y_max = float('-inf')

    for point in data:
        x_min = min(point[0], x_min)
        x_max = max(point[0], x_max)
        y_min = min(point[1], y_min)
        y_max = max(point[1], y_max)

    centroids = []
    for i in range(k):
        centroids.append([random_sample(x_min, x_max),
                            random_sample(y_min, y_max)])

    return centroids


def get_distance(point_1, point_2):
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5


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
    new_centroids = [[0, 0] for i in range(k)]
    counts = [0] * k

    for point, label in zip(points, labels):
        new_centroids[label][0] += point[0]
        new_centroids[label][1] += point[1]
        counts[label] += 1
    try:
        for i, (x, y) in enumerate(new_centroids):
            new_centroids[i] = (x/counts[i], y/counts[i])
    except:
        pass
    return new_centroids


def should_stop(old_centroids, new_centroids, threshold=1e-5):
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

    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='red')
    plt.show()


values = pd.read_csv("dataset_very_cool.csv")
dataset = values[['A', 'B']].to_numpy()

main(dataset, 2)
