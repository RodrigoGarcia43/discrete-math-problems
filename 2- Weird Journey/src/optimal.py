# Función principal
# Entradas:
# n -> Cantidad de vértices
# m -> Cantidad de aristas
# edges -> Lista de tuplas que representan las aristas
def solve(n, m, edges):

    visited = [0] * n
    vertices = [[] for _ in range(n)]

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
            vertices[u].append(v)

    # Verificando si el grafo es conexo, de no serlo se retorna 0.
    dfs(visited, vertices, 0)
    for v in visited:
        if v == 0:
            return 0

    result = 0

    # Lista para guardar los factoriales hasta el máximo valor que será necesario y evitar recalculos.
    factorials_list = factorials(max(loops, max(cnt)))

    # Calculando parejas de aristas no lazos adyacentes.
    for c in cnt:
        result += combinations(c, 2, factorials_list)

    # se le suma la cantidad de lazos, multiplicada por m-1.
    result += loops * (m - 1)

    # Quitando pares de aristas lazos que fueron incluidos dos veces.
    result -= combinations(loops, 2, factorials_list)
    return result


def combinations(n, k, factorials):
    return int(factorials[n] / (factorials[n - k] * factorials[k]))


def factorials(n):
    factorial_list = [1] * (n + 2)
    fact = 1
    for i in range(1, n + 2):
        fact = fact * i
        factorial_list[i] = fact

    return factorial_list


def dfs(visited, graph, node):
    visited[node] = 1
    for neighbour in graph[node]:
        if visited[neighbour] == 0:
            dfs(visited, graph, neighbour)

