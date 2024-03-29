import numpy as np

nodes = [
    [0, 1],
    [3, 2],
    [4, 1],
    [2, 4],
    [1, 2],
    [0, 2],
    [3, 1],
    [1, 4],
    [4, 3],
    [1, 3],
    [2, 0]
]

n = int(input("Enter the number of edges:\n"))

print(f"Enter the {n} edges:\n")
for x in range(0, n):
    print(f"Enter nodes of edge {x+1}")
    for y in range(0, 2):
        nodes[x][y] = int(input())
    print()


nodes = np.array(nodes)
adjacency_matrix = np.zeros((np.max(nodes)+1, np.max(nodes)+1))
for s, e in nodes:
    adjacency_matrix[s][e] = 1

hits = np.ones((np.max(nodes)+1,))
authorities = np.ones((np.max(nodes)+1,))

print(f"The adjacency matrix is:\n{adjacency_matrix}\n")

max_itr = 10
for _ in range(max_itr):
    hits = np.dot(adjacency_matrix, authorities)
    authorities = np.dot(adjacency_matrix.T, hits)

    # normalize
    authorities = authorities / np.linalg.norm(authorities)
hits = hits / np.linalg.norm(hits)
print("Hubs: ", dict(enumerate(hits)))
print()
print("Authorities: ", dict(enumerate(authorities)))
print()
print(
    f"The highest ranking page is {np.argmax(authorities)}")




https://github.com/priyanshpsalian
