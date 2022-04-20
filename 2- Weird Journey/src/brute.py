# Función principal
# Entradas:
# n -> Cantidad de vértices
# m -> Cantidad de aristas
# edges -> Lista de tuplas que representan las aristas
def solve(n, m, edges):
    vertices = [[0] * n for _ in range(n)]
    visited = [0] * n

    graph = [[] for _ in range(n)]
    for v, u in edges:
        v, u = v - 1, u - 1
        if v == u:
            graph[v].append(u)
        else:
            graph[v].append(u)
            graph[u].append(v)

        vertices[v][u] = vertices[u][v] = 2

    # Verificando si el grafo es conexo, de no serlo se retorna 0.
    dfs(visited, graph, 0)
    for v in visited:
        if v == 0:
            return 0

    # En rests quedarán finalmente los caminos válidos, representados por las dos aristas
    # por las que se camina una sola vez.
    rests = []
    for i in range(n):
        calculate_from_vertex(n, m, vertices, i, rests)

    return len(rests)


# Función para analizar los caminos válidos a partir del vértice i y guardarlos en rests.
def calculate_from_vertex(n, m, vertices, actual, rests, count=0):
    # Caso base que se alcanza cuando se ha caminado (2 * m) - 2 veces.
    if count == (2 * m) - 2:
        rest = []
        # Verificando si fue un camino válido y si no había sido guardado anteriormente.
        for i in range(n):
            for j in range(n):
                if (
                    (vertices[i][j] == 1)
                    and (not ((i, j) in rest))
                    and (not ((j, i) in rest))
                ):
                    rest.append((i, j))

        if not (rest in rests) and len(rest) == 2:
            rests.append(rest)
        return

    for i in range(0, n):
        # Buscando aristas adyacentes al vértice actual que todavía se puedan caminar para hacer un llamado recursivo.
        if vertices[actual][i] > 0:
            vertices[actual][i] -= 1
            if i != actual:
                vertices[i][actual] -= 1
            calculate_from_vertex(n, m, vertices, i, rests, count + 1)
            vertices[actual][i] += 1
            if i != actual:
                vertices[i][actual] += 1

    return


def dfs(visited, graph, node):
    if visited[node] == 0:
        visited[node] = 1
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

