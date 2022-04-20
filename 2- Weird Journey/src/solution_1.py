# Función principal
# Entradas:
# n -> Cantidad de vértices
# m -> Cantidad de aristas
# edges -> Lista de tuplas que representan las aristas
def solve(n, m, edges):
    visited = [0] * n
    vertices = [[0] * n for _ in range(n)]

    for v, u in edges:
        v, u = v - 1, u - 1
        if v == u:
            vertices[v].append(u)

        else:
            vertices[v].append(u)
            vertices[u].append(v)

    # Verificando si el grafo es conexo, de no serlo se retorna 0.
    dfs(visited, vertices, 0)
    for v in visited:
        if v == 0:
            return 0

    degrees = []
    for v in vertices:
        degrees.append(len(v))

    result = 0
    # Por cada pareja de aristas del grafo se analizan los grados de los cuatro vértices participantes.
    # Si se cumple con las condiciones del análisis, el valor a retornar aumenta en uno,
    # pues se encuentra un camino válido.
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            result += analyze_degrees(edges[i], edges[j])

    return result


# Función para analizar si tomando a dos aristas como las de una sola pasada se forma un camino válido.
def analyze_degrees(edge1, edge2):
    v1, v2, v3, v4 = edge1[0], edge1[1], edge2[0], edge2[1]
    _set = set([v1, v2, v3, v4])
    if len(_set) == 3 or len(_set) == 2:
        return 1
    else:
        return 0


def dfs(visited, graph, node):
    if visited[node] == 0:
        visited[node] = 1
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# print(solve(5, 7, [(1, 2), (2, 2), (4, 1), (5, 1), (3, 2), (2, 4), (3, 3)]))
