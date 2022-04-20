import sys
from floyd_warshall import floyd_warshall


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
    distances = floyd_warshall(edges, n)

    for i in range(n):

        for j in range(i + 1, n):

            walked = []
            calculate(vertices, edges, i, i, j, distances, walked)
            results.append(len(walked))

    return results


# A diferencia del algoritmo original, no es necesario llevar la cuenta del cost.
# Se entra la lista "distances" con las distancias entre todos los pares de vértices.
def calculate(
    vertices,
    edges,
    start,
    actual,
    dest,
    distances,
    walked,
    visited=None,
    local_walked=[],
):

    if actual == dest:
        for u, v in local_walked:
            if (u, v) not in walked and (v, u) not in walked:
                walked.append((u, v))
        return

    if visited is None:
        visited = [0] * len(vertices)
        visited[actual] = 1

    for i in range(len(vertices)):
        # Si caminar hacia una arista adyacente provoca que el camino actual deje de ser de costo mínimo,
        #  entonces no es necesario hacerlo.
        if (
            visited[i] == 0
            and vertices[actual][i] == 1
            and distances[start][actual] + edges[actual][i] + distances[i][dest]
            == distances[start][dest]
        ):
            visited[i] = 1
            local_walked.append((actual, i))

            calculate(
                vertices,
                edges,
                start,
                i,
                dest,
                distances,
                walked,
                visited,
                local_walked,
            )

            local_walked.remove((actual, i))

            visited[i] = 0

