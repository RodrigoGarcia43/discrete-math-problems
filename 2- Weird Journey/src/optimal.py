import sys


def solve(n, m, edges):

    visited = [0] * n
    vertices = []
    for _ in range(n):
        vertices.append([])

    cnt = [0] * n
    loops = 0

    for v, u in edges:
        v, u = v - 1, u - 1

        if v == u:
            loops += 1
            vertices[v].append(u)

        else:
            cnt[v] += 1
            cnt[u] += 1
            vertices[v].append(u)
            vertices[v].append(v)

    dfs(visited, vertices, 0)
    for v in visited:
        if v == 0:
            return 0

    result = 0

    for c in cnt:
        result += combinations(c, 2)

    result += loops * (m - 1)
    result -= combinations(loops, 2)
    return result


def combinations(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def dfs(visited, graph, node):
    if visited[node] == 0:
        visited[node] = 1
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print(solve(5, 3, [(1, 2), (2, 3), (4, 5)]))
