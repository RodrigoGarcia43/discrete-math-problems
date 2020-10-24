import sys


def select(visited, distances, n):
    v = -1
    for i in range(0, n):
        if visited[i] == 0 and (v < 0 or distances[i] <= distances[v]):
            v = i
    return v


def dijkstras(vertices, edges):
    n = len(vertices[0])

    visited = [0] * n
    distances = [sys.maxsize] * n
    distances[0] = 0

    while True:
        v = select(visited, distances, n)
        if v == -1:
            break

        for i in range(0, n):

            if vertices[v][i] == 1 and visited[v] == 0:
                new_distance = distances[v] + edges[v][i]

                if distances[i] > new_distance:
                    distances[i] = new_distance

        visited[v] = 1

    return distances

