import random


def generator():
    for i in range(0, 10000):
        aux = "test" + str(i)
        f = open("tests/" + aux, "w")

        n = random.randint(5, 30)
        m = random.randint(1, int((n * (n - 1) / 2)))
        edges = []

        for _ in range(0, m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            if (not (u, v) in edges) and not ((v, u) in edges):
                edges.append((u, v))

        m = len(edges)

        print(n, file=f)
        print(m, file=f)
        print(edges, file=f)

        f.close()


generator()
