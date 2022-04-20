import random


def generator():
    for i in range(0, 10000):
        aux = "test" + str(i)
        f = open("tests/" + aux, "w")

        n = random.randint(3, 12)
        m = random.randint(2, n)
        t_edges = []
        s_edges = []

        count = 2
        actual = 1
        while count < n + 1:
            _count = count + 1
            if actual == _count:
                _count += 1
            temp = random.randint(_count, n + 1)
            for i in range(count, temp):
                s_edges.append((actual, i))
            count = temp
            actual += 1

        count = 2
        actual = 1
        while count < m + 1:
            _count = count + 1
            if actual == _count:
                _count += 1
            temp = random.randint(_count, m + 1)
            for i in range(count, temp):
                t_edges.append((actual, i))
            count = temp
            actual += 1

        print(n, file=f)
        print(s_edges, file=f)
        print(m, file=f)
        print(t_edges, file=f)

        f.close()


generator()
