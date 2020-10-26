import sys


def solve(n, m, edges):

    temp = [0] * (n)
    vertices = []
    for _ in range(n):
        vertices.append(list.copy(temp))

    for v, u in edges:
        vertices[v - 1][u - 1] = vertices[u - 1][v - 1] = 2

    rests = []
    for i in range(n):
        calculate_from_vertex(n, m, vertices, i, rests)

    return len(rests)


def calculate_from_vertex(n, m, vertices, actual, rests, count=0):
    if count == (2 * m) - 2:
        rest = []
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
        if vertices[actual][i] > 0:
            vertices[actual][i] -= 1
            if i != actual:
                vertices[i][actual] -= 1
            calculate_from_vertex(n, m, vertices, i, rests, count + 1)
            vertices[actual][i] += 1
            if i != actual:
                vertices[i][actual] += 1

    return


def search_for_invalid(rest):
    for i in range(len(rest)):
        for j in range(len(rest)):
            if rest[i][j] == 2:
                return True
    return False


print(solve(5, 3, [(1, 2), (2, 3), (4, 5)]))

