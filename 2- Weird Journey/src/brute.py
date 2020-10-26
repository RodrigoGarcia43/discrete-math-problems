import sys


def solve(n, m, edges, count=0):

    temp = [0] * (n)
    vertices = []
    for _ in range(0, m + 1):
        vertices.append(list.copy(temp))

    for v, u in edges:
        vertices[v][u] = vertices[u][v] = 1

