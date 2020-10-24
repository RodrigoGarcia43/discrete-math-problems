import sys
from dijkstras import dijkstras


def analyze(n, m, initial_x, initial_y, dest, instant_positions):
    nodes = {}
    nodes[0] = (initial_x, initial_y)
    for index in range(1, m + 1):
        nodes[index] = instant_positions[index - 1]

    temp = [-1] * (m + 1)
    vertices = []
    edges = []
    for _ in range(0, m + 1):
        vertices.append(list.copy(temp))
        edges.append(list.copy(temp))

    to_sort_by_x = []
    to_sort_by_y = []
    for key, pos in nodes.items():
        x, y = pos
        to_sort_by_x.append((x, y, key))
        to_sort_by_y.append((y, x, key))

    sorted_by_x = sorted(to_sort_by_x)
    sorted_by_y = sorted(to_sort_by_y)

    for i in range(0, m):
        x, _, v = sorted_by_x[i]
        next_x, _, next_v = sorted_by_x[i + 1]

        vertices[v][next_v] = 1
        vertices[next_v][v] = 1

        new_distance = abs(x - next_x)

        if new_distance < edges[v][next_v] or edges[v][next_v] == -1:
            edges[v][next_v] = new_distance
            edges[next_v][v] = new_distance

        y, _, v = sorted_by_y[i]
        next_y, _, next_v = sorted_by_y[i + 1]

        vertices[v][next_v] = 1
        vertices[next_v][v] = 1

        new_distance = abs(y - next_y)

        if new_distance < edges[v][next_v] or edges[v][next_v] == -1:
            edges[v][next_v] = new_distance
            edges[next_v][v] = new_distance

    distances = dijkstras(vertices, edges)

    for i in range(0, len(distances)):
        distances[i] += abs(nodes[i][0] - dest[0]) + abs(nodes[i][1] - dest[1])

    return min(distances)


# print(analyze(84, 5, 67, 59, (41, 2), [(39, 56), (7, 2), (15, 3), (74, 18), (22, 7)],))

