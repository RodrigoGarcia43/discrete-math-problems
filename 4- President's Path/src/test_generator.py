import random


def generator():
    for i in range(0, 10000):
        aux = "test" + str(i)
        f = open("tests/" + aux, "w")

        n = random.randint(5, 10)
        m = random.randint(3, int((n * (n - 1) / 2)))
        # m = random.randint(5, 10)
        edges = []

        while len(edges) == 0:
            edges = []
            li = []
            for _ in range(0, m):
                u = random.randint(1, n)
                v = random.randint(1, n)
                l = random.randint(1, 50)
                if (not (u, v) in li) and not ((v, u) in li) and u != v:
                    li.append((u, v))
                    edges.append((u, v, l))

        m = len(edges)

        print(n, file=f)
        print(m, file=f)
        print(edges, file=f)

        f.close()


generator()
