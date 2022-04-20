import sys
from floyd_warshall import floyd_warshall

# Función principal
# Entradas:
# n -> Cantidad de vértices del grafo
# m -> Cantidad de aristas del grafo
# roads -> Lista de tuplas que representan las aristas
def solve(n, m, roads):
    edges = [[sys.maxsize] * (n) for _ in range(n)]
    vertices = [[0] * (n) for _ in range(n)]

    for x, y, l in roads:
        x, y = x - 1, y - 1
        vertices[x][y] = vertices[y][x] = 1
        edges[x][y] = edges[y][x] = l

    for i in range(n):
        edges[i][i] = 0

    results = []
    # Calculando distancia entre cada par de vértices
    distances = floyd_warshall(edges, n)

    for i in range(n):
        for j in range(i + 1, n):
            # Para cada par de vértices del grafo, se pasa por todos los caminos de uno a otro y
            # se guarda en walked todas las aristas que participen en alguno de costo mínimo.
            walked = []
            calculate(vertices, edges, i, j, distances[i][j], walked)
            results.append(len(walked))

    return results


# Función para almacenar en "walked" todas las aristas que participen en algún camino
# de costo "distance" entre el nodo "actual" y el nodo "dest"
def calculate(
    vertices,
    edges,
    actual,
    dest,
    distance,
    walked,
    visited=None,
    cost=0,
    local_walked=[],
):

    # Caso base que se alcanza al llegar al nodo destino.
    # Si el camino recorrido fue mínimo, se guarda en "walked", todas las aristas pertenecientes a "local_walked"
    # que no pertenecieran ya a este.
    if actual == dest:
        if cost == distance:
            for u, v in local_walked:
                if (u, v) not in walked and (v, u) not in walked:
                    walked.append((u, v))
            return
        else:
            return

    if visited is None:
        visited = [0] * len(edges)
        visited[actual] = 1

    # Se camina hacia los nodos adyacentes a actual que no fueron ya visitados, aumentando el costo
    # del camino recorriéndose actualmente.
    for i in range(len(edges)):
        if visited[i] == 0 and vertices[actual][i] == 1:
            visited[i] = 1
            local_walked.append((actual, i))

            calculate(
                vertices,
                edges,
                i,
                dest,
                distance,
                walked,
                visited,
                cost + edges[actual][i],
                local_walked,
            )

            local_walked.remove((actual, i))

            visited[i] = 0

