def floyd_warshall(graph, n):
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(n):
        for u in range(n):
            for v in range(n):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])

    return distance

