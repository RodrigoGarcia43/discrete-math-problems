import sys
from floyd_warshall import floyd_warshall

# Función principal
# Entradas:
# n -> Cantidad de vértices del grafo
# m -> Cantidad de aristas del grafo
# roads -> Lista de tuplas que representan las aristas
def solve(n, m, roads):
    edges = [[sys.maxsize] * (n) for _ in range(n)]

    for i in range(n):
        edges[i][i] = 0

    for x, y, l in roads:
        x, y = x - 1, y - 1
        edges[x][y] = edges[y][x] = l

    distances = floyd_warshall(edges, n)

    # inEdges almacena para cada vértice, la cantidad de aristas que van hacia él y que participan en un
    # camino de costo mínimo desde cada vértice del grafo.
    inEdges = [[0] * (n) for _ in range(n)]
    for u, v, cst in roads:
        u, v = u - 1, v - 1
        for k in range(n):
            if distances[k][u] + cst == distances[k][v]:
                inEdges[k][v] += 1
            if distances[k][v] + cst == distances[k][u]:
                inEdges[k][u] += 1

    # Para cada par de vértices u, v. para cada vértice k. Si k participa en un camino de costo mínimo de u a v,
    # entones a la respuesta perteneciente a la posición de u,v se le adiciona la cantidad de inEdges de k, saliendo de u.
    result = []
    for u in range(n):
        for v in range(u + 1, n):
            count = 0
            for k in range(n):
                if distances[u][k] + distances[k][v] == distances[u][v]:
                    count += inEdges[u][k]
            result.append(count)

    return result

